import uuid

from django.db import models
from django.utils import timezone


class QRSession(models.Model):

    STATUS_CHOICES = [
        ("REGISTER", "Register"),
        ("LOGIN", "Login"),
        ("EXPIRED", "Expired"),
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

    expires_at = models.DateTimeField(
        null=True,
        blank=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    updated_at = models.DateTimeField(
        auto_now=True
    )

    def is_expired(self):

        if self.expires_at is None:
            return False

        return timezone.now() >= self.expires_at

    def __str__(self):
        return f"{self.session_key} - {self.status}"