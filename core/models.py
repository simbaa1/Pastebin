from django.db import models
from django.contrib.auth.models import User


class Paste(models.Model):
    UNLISTED = "UL"
    PUBLIC = "PB"
    PRIVATE = "PR"

    EXPIRY_OPTIONS = {
        UNLISTED: "Unlisted",
        PUBLIC: "Public",
        PRIVATE: "Private"
    }

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    paste_exposure = models.CharField(
        max_length=10, choices=EXPIRY_OPTIONS, default=UNLISTED
    )
    expiry_date = models.DateTimeField(blank=True, null=True)
    title = models.CharField(max_length=250, blank=True, null=True)
    burn_after_reading = models.BooleanField(default=False)
    password = models.BooleanField(default=False)
    password_text = models.CharField(blank=True, null=True, max_length=250)
