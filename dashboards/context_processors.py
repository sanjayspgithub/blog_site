from django.contrib.auth.models import User
from blogs.models import Blog, Category

def dashboard_counts(request):
    return {
        'category_count': Category.objects.all().count(),
        'blog_count': Blog.objects.all().count(),
        'total_users_count': User.objects.count(),
        'published_posts_count': Blog.objects.filter(status='published').count(),
        'draft_posts_count': Blog.objects.filter(status='draft').count(),
        'pending_posts_count': Blog.objects.filter(status='pending').count(),
    }