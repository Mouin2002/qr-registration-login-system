from django.shortcuts import render

# Create your views here.
from django.contrib.auth import get_user_model
from django.shortcuts import render, redirect

from .forms import RegistrationForm


User = get_user_model()


def register(request):

    if request.method == "POST":
        form = RegistrationForm(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            user.set_password(
                form.cleaned_data["password"]
            )

            user.save()

            return redirect("register_success")

    else:
        form = RegistrationForm()

    return render(
        request,
        "users/register.html",
        {"form": form}
    )


def register_success(request):
    return render(
        request,
        "users/register_success.html"
    )