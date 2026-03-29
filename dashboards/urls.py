from django.urls import path
from . import views



urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    # Category crud
    path('categorie/', views.categorie, name='categorie'),
    path('categorie/add/', views.add_category, name='add_category'),
    path('categorie/delete/<int:id>/', views.delete_category, name='delete_category'),
    path('categorie/edit/<int:id>/', views.edit_category, name='edit_category'),
    # blog crud
    path('blogs/', views.blog, name='blog'),
    path('users_blogs/', views.user_blog, name='user_blog'),
    path('blogs/add/', views.add_blog, name='add_blog'),
    path('blogs/edit/<int:id>', views.edit_blog, name='edit_blog'),
    path('blogs/delete/<int:id>', views.delete_blog, name='delete_blog'),
    # user crud
    path('user/', views.user, name='user'),
    path('user/add', views.add_user, name='add_user'),
    path('user/edit/<int:id>/', views.edit_user, name='edit_user'),
    path('user/delete/<int:id>', views.delete_user, name='delete_user'),
]
