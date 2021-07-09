from re import search
from django.contrib import admin
from .models import Tag

admin.site.register(Tag)

class TagAdmin(admin.ModelAdmin):
    search_field = ['label']