from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name="api-overview"),
    path('books/', views.bookList, name="books"),
    path('book_selected/<str:pk>/', views.bookSelected, name="book_selected"),
    path('book_add/', views.bookAdd, name="book_add"),
    path('book_update/<str:pk>/', views.bookUpdate, name="book_update"),
    path('book_delete/<str:pk>/', views.bookDelete, name="book_update")
]

