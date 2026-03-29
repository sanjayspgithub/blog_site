

from django.contrib import admin
from .models import About, Category, Blog, Social, Comment

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}  #shortcut feature to automatically fill the slug field
    list_display = ('title', 'category', 'author', 'status', 'created_at')
    # list_filter = ('status', 'created_at', 'author')
    search_fields = ('title', 'category__category_name', 'status')

class AboutAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        count = About.objects.all().count()
        if count == 0:
            return True
        return False
    
class CommentAdmin(admin.ModelAdmin):
    list_display = ('comment', 'user', 'blog', 'created_at')


admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(Social)
admin.site.register(Comment, CommentAdmin)
