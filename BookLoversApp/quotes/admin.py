from django.contrib import admin

from BookLoversApp.quotes.models import Quote


@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    list_display = ['quote_text', 'date_and_time_of_publication', 'book', 'user']
    ordering = ['date_and_time_of_publication']
    list_filter = ['book', 'user']
    search_fields = ['quote_text__startswith']

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        form.base_fields["quote_text"].label = "Input Quote:"
        form.base_fields["book"].label = "This quote is from book:"
        form.base_fields["user"].label = "Creator of Quote:"
        return form
