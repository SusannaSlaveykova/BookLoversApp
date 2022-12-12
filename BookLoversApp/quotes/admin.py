from django.contrib import admin

from BookLoversApp.quotes.models import Quote


@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ['quote_text', 'date_and_time_of_publication', 'book', 'user']
    ordering = ['date_and_time_of_publication']
    list_filter = ['book']
