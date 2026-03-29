from django.urls import path
from . import views



urlpatterns = [
    path('<int:id>/', views.category_posts, name='category_posts'),
]
