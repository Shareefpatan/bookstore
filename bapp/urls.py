from django.contrib import admin
from .import views
from django.urls import path,include
from bapp.views import base,main,detail,form,rent_book,returned,return_view,cancel_view

app_name='bapp'
urlpatterns = [
    path('',base,name='base'),
    #path('cancel/',cancel,name=cancel),
    path('detail/<int:book_id>/', detail, name='detail'),
    path('order/<int:book_id>/', views.order, name='order'),
    path('main/',main,name='main'),
    path('form/',form,name='form'),
    path('success/',return_view,name='return_view'),
    path('cancel/',cancel_view,name='cancel_view'),
    path('rent-book/<int:book_id>/', rent_book, name='rent_book'),
    path('returned/',returned,name='returned'),
    path('book/<int:book_id>/add_review/', views.add_review, name='add_review'),
    path('review/<int:review_id>/edit/', views.edit_review, name='edit_review'),
    path('review/<int:review_id>/delete/', views.delete_review, name='delete_review'),
    path('book/<int:pk>/', views.book_detail, name='book_detail'),
    path('accounts/', include('django.contrib.auth.urls')),
   
   


]