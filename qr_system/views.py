import base64
from datetime import timedelta
from io import BytesIO

import qrcode

from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, render
from django.utils import timezone

from .models import QRSession


def generate_qr_base64(data):

    qr = qrcode.make(data)

    buffer = BytesIO()

    qr.save(
        buffer,
        format="PNG"
    )

    return base64.b64encode(
        buffer.getvalue()
    ).decode("utf-8")


def qr_screen(request):

    qr_session = QRSession.objects.create(
        status="REGISTER",
        expires_at=(
            timezone.now()
            + timedelta(minutes=5)
        )
    )

    register_url = (
        f"http://{settings.QR_HOST}:8000"
        f"/register/{qr_session.session_key}/"
    )

    login_url = (
        f"http://{settings.QR_HOST}:8000"
        f"/login/{qr_session.session_key}/"
    )

    register_qr_base64 = generate_qr_base64(
        register_url
    )

    login_qr_base64 = generate_qr_base64(
        login_url
    )

    status_url = (
        f"/qr/status/{qr_session.session_key}/"
    )

    return render(
        request,
        "qr_system/qr_screen.html",
        {
            "qr_session": qr_session,
            "register_qr_base64": register_qr_base64,
            "login_qr_base64": login_qr_base64,
            "register_url": register_url,
            "login_url": login_url,
            "status_url": status_url,
        }
    )


def qr_status(request, session_key):

    qr_session = get_object_or_404(
        QRSession,
        session_key=session_key
    )

    if qr_session.is_expired():

        qr_session.status = "EXPIRED"

        qr_session.save(
            update_fields=[
                "status",
                "updated_at"
            ]
        )

    return JsonResponse({
        "status": qr_session.status
    })