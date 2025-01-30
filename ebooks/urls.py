from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
from django.urls import path
from . import views

urlpatterns = [
    path('', views.ebook_list, name='ebook_list'),
    path('create/', views.create_ebook, name='create_ebook'),
    path('update/<int:pk>/', views.update_ebook, name='update_ebook'),
    path('delete/<int:pk>/', views.delete_ebook, name='delete_ebook'),
]
