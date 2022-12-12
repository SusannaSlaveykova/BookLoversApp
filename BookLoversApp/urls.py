from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('BookLoversApp.accounts.urls')),
    path('books/', include('BookLoversApp.books.urls')),
    path('', include('BookLoversApp.common.urls')),
    path('beloved_characters/', include('BookLoversApp.beloved_characters.urls')),
    path('quotes/', include('BookLoversApp.quotes.urls'))

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
