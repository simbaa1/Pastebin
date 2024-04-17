from django.contrib import admin
from .models import Tag, Paste
# Register your models here.

class PasteAdmin(admin.ModelAdmin):
    pass

admin.site.register(Paste, PasteAdmin)