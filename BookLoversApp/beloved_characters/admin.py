from django.contrib import admin

from BookLoversApp.beloved_characters.models import BelovedCharacter


@admin.register(BelovedCharacter)
class BelovedCharacterAdmin(admin.ModelAdmin):
    list_display = ['name', 'reason_to_like', 'favourite_story', 'book', 'user']
    ordering = ['name']
    list_filter = ['name', 'book']
    search_fields = ['name__startswith']