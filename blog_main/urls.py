"""
URL configuration for blog_main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""



from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

from blogs import views as Blogsview

from django.contrib.auth import views as auth_views

# Custom LoginView for role-based redirect
class MyLoginView(auth_views.LoginView):
    template_name = 'login.html'

    def get_success_url(self):
        # staff → dashboard
        if self.request.user.is_staff:
            return '/dashboard/'
        # normal user → home
        return '/'

urlpatterns = [
    path('secure-admin/', admin.site.urls),
    path('', views.home, name='home'),

    path('category/', include('blogs.urls')),
    path('search/', Blogsview.search, name='search'),
    path('blog/<slug:slug>/', Blogsview.sblogs, name='sblogs'),
    # user add blog
    path('add_blog/', Blogsview.add_b, name="add_b"),
    path('add_blog_form/', Blogsview.add_blog_f, name="add_blog_f"),
    path('ai-suggest/', views.ai_suggest, name='ai_suggest'),
    path('edit_blog_form/<int:id>/', Blogsview.edit_blog_f, name="edit_blog_f"),
    path('user_delete_blog/<int:id>/', Blogsview.user_delete_blog, name='user_delete_blog'),

    path('register/', views.register, name='register'),
    path('login/', MyLoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    path('dashboard/', include('dashboards.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

