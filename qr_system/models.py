from django.db import models

# Create your models here.
import uuid

from django.db import models


class QRSession(models.Model):

    STATUS_CHOICES = [
        ("REGISTER", "Register"),
        ("LOGIN", "Login"),
    ]

    session_key = models.UUIDField(
        default=uuid.uuid4,
        unique=True,
        editable=False
    )

    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default="REGISTER"
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return f"{self.session_key} - {self.status}"