from django.contrib import admin
from django.urls import path, include

from ebooks import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('ebooks.urls')),
    path('create_book/', views.create_book, name='create_book'),  # URL for creating new books

]