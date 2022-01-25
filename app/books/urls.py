from django.urls import path
from books import views as books_views
from django.conf.urls.static import static
from django.conf import settings
from . import views

urlpatterns = [
    path('', views.home, name='bookstore-home'),
    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)