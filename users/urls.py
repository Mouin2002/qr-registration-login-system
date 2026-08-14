from django.urls import path

from . import views


urlpatterns = [

    path(
        "register/<uuid:session_key>/",
        views.register,
        name="register"
    ),

    path(
        "register/success/",
        views.register_success,
        name="register_success"
    ),

    path(
        "login/<uuid:session_key>/",
        views.login_view,
        name="login"
    ),

    path(
        "dashboard/",
        views.dashboard,
        name="dashboard"
    ),
]