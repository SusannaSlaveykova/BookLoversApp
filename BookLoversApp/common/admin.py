from django.contrib import admin

from BookLoversApp.common.models import Comment


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['comment', 'date_and_time_of_publication', 'book', 'user']
    ordering = ['date_and_time_of_publication']
    list_filter = ['user', 'book']
    search_fields = ['comment__startswith']
