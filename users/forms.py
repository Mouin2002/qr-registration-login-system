import re

from django import forms

from .models import User


class RegistrationForm(forms.ModelForm):

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Enter your password"
            }
        )
    )

    confirm_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Confirm your password"
            }
        )
    )

    class Meta:

        model = User

        fields = [
            "name",
            "email",
            "phone",
        ]

        widgets = {

            "name": forms.TextInput(
                attrs={
                    "placeholder": "Enter your name"
                }
            ),

            "email": forms.EmailInput(
                attrs={
                    "placeholder": "Enter your email"
                }
            ),

            "phone": forms.TextInput(
                attrs={
                    "placeholder": "Enter your phone number"
                }
            ),
        }


    def clean_name(self):

        name = self.cleaned_data["name"].strip()

        if len(name) < 3:

            raise forms.ValidationError(
                "Name must contain at least 3 characters."
            )

        if not re.fullmatch(
            r"[A-Za-z ]+",
            name
        ):

            raise forms.ValidationError(
                "Name can contain only letters and spaces."
            )

        return name


    def clean_email(self):

        email = self.cleaned_data["email"].strip().lower()

        if User.objects.filter(
            email=email
        ).exists():

            raise forms.ValidationError(
                "This email is already registered."
            )

        return email


    def clean_phone(self):

        phone = self.cleaned_data["phone"].strip()

        if not re.fullmatch(
            r"[6-9][0-9]{9}",
            phone
        ):

            raise forms.ValidationError(
                "Enter a valid 10-digit phone number."
            )

        return phone


    def clean_password(self):

        password = self.cleaned_data["password"]

        if len(password) < 8:

            raise forms.ValidationError(
                "Password must contain at least 8 characters."
            )

        if not re.search(
            r"[A-Z]",
            password
        ):

            raise forms.ValidationError(
                "Password must contain at least one uppercase letter."
            )

        if not re.search(
            r"[a-z]",
            password
        ):

            raise forms.ValidationError(
                "Password must contain at least one lowercase letter."
            )

        if not re.search(
            r"[0-9]",
            password
        ):

            raise forms.ValidationError(
                "Password must contain at least one number."
            )

        if not re.search(
            r"[^A-Za-z0-9]",
            password
        ):

            raise forms.ValidationError(
                "Password must contain at least one special character."
            )

        return password


    def clean(self):

        cleaned_data = super().clean()

        password = cleaned_data.get(
            "password"
        )

        confirm_password = cleaned_data.get(
            "confirm_password"
        )

        if (
            password
            and confirm_password
            and password != confirm_password
        ):

            raise forms.ValidationError(
                "Passwords do not match."
            )

        return cleaned_data