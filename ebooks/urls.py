from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Home page where books are listed
    path('update_book/', views.update_book, name='update_book'),  # URL to handle book update

    path('delete_book/', views.delete_book, name='delete_book'),  # URL to handle book deletion

]