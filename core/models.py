from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.utils.crypto import get_random_string
from random import randint


class Tag(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(null=True, blank=True, unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Tags"


class Paste(models.Model):
    UNLISTED = "UL"
    PUBLIC = "PB"
    PRIVATE = "PR"

    EXPIRY_OPTIONS = {
        UNLISTED: "Unlisted",
        PUBLIC: "Public",
        PRIVATE: "Private"
    }

    author = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)
    content = models.TextField()
    slug = models.SlugField(unique=True, blank=True)
    paste_exposure = models.CharField(
        max_length=10, choices=EXPIRY_OPTIONS, default=UNLISTED
    )
    expiry_date = models.DateTimeField(blank=True, null=True)
    title = models.CharField(max_length=250, blank=True,
                             null=True, default="Untitled")
    burn_after_reading = models.BooleanField(default=False)
    password = models.BooleanField(default=False)
    password_text = models.CharField(blank=True, null=True, max_length=250)
    tags = models.ManyToManyField(Tag, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.content}"

    def save(self, *args, **kwargs):

        if not self.slug:
            string_to_slugify = f'{get_random_string(8)} {randint(1, 30)}'
            self.slug = slugify(string_to_slugify)[:8]
            
            i = 0
            while Paste.objects.filter(slug=self.slug).exists():
                self.slug = string_to_slugify[:8+i]

        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Pastes"
