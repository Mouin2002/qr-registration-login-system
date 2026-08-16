from django.contrib.auth import authenticate, get_user_model
from django.shortcuts import get_object_or_404, redirect, render

from .forms import RegistrationForm
from qr_system.models import QRSession


User = get_user_model()


def register(request, session_key):

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

        return render(
            request,
            "users/qr_expired.html"
        )

    if qr_session.status != "REGISTER":

        return render(
            request,
            "users/qr_expired.html"
        )

    if request.method == "POST":

        form = RegistrationForm(
            request.POST
        )

        if form.is_valid():

            user = form.save(
                commit=False
            )

            user.set_password(
                form.cleaned_data["password"]
            )

            user.save()

            qr_session.status = "LOGIN"

            qr_session.save(
                update_fields=[
                    "status",
                    "updated_at"
                ]
            )

            return redirect(
                "register_success"
            )

    else:

        form = RegistrationForm()

    return render(
        request,
        "users/register.html",
        {
            "form": form
        }
    )


def register_success(request):

    return render(
        request,
        "users/register_success.html"
    )


def login_view(request, session_key):

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

        return render(
            request,
            "users/qr_expired.html"
        )

    # Only LOGIN QR can be used.
    if qr_session.status != "LOGIN":

        return render(
            request,
            "users/qr_expired.html"
        )

    error_message = None

    if request.method == "POST":

        email = request.POST.get(
            "email",
            ""
        ).strip().lower()

        password = request.POST.get(
            "password",
            ""
        )

        if not email or not password:

            error_message = (
                "Email and password are required."
            )

        else:

            user = authenticate(
                request,
                username=email,
                password=password
            )

            if user is not None:

                # Create Django session.
                request.session["user_id"] = user.id

                # Make this QR session single-use.
                qr_session.status = "COMPLETED"

                qr_session.save(
                    update_fields=[
                        "status",
                        "updated_at"
                    ]
                )

                return redirect(
                    "dashboard"
                )

            error_message = (
                "Invalid email or password."
            )

    return render(
        request,
        "users/login.html",
        {
            "qr_session": qr_session,
            "error_message": error_message,
        }
    )


def dashboard(request):

    user_id = request.session.get(
        "user_id"
    )

    if not user_id:

        return redirect(
            "qr_screen"
        )

    user = get_object_or_404(
        User,
        id=user_id
    )

    return render(
        request,
        "users/dashboard.html",
        {
            "user": user
        }
    )

def logout_view(request):

    request.session.flush()

    return redirect(
        "qr_screen"
    )