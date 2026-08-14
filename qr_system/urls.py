from django.urls import path

from . import views


urlpatterns = [
    path(
        "",
        views.qr_screen,
        name="qr_screen"
    ),

    path(
        "status/<uuid:session_key>/",
        views.qr_status,
        name="qr_status"
    ),
]