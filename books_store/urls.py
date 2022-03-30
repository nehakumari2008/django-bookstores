from django.urls import path, include

from . import views

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', views.register, name='register'),

    path('', views.index, name='index'),

    path('store/', views.get_store, name='stores'),
    path('store/create/', views.create_store, name='create_store'),
    path('store/<int:store_id>/edit/', views.edit_store, name='edit_store'),
    path('store/<int:store_id>/delete/', views.delete_store, name='delete_store'),
    path('store/<int:store_id>/books/', views.get_books, name='books'),
    path('store/<int:store_id>/books/create/', views.create_book, name='create_book'),
    path('store/<int:store_id>/books/<int:book_id>/', views.get_book, name='book'),
    path('store/<int:store_id>/books/<int:book_id>/edit/', views.edit_book, name='edit_book'),
    path('store/<int:store_id>/books/<int:book_id>/delete/', views.delete_book, name='delete_book'),

]