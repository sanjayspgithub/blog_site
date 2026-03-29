
from django import forms
from .models import Blog



class UserAddBlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = [  'title',
                    'category',
                    'featured_image',
                    'short_description',
                    'blog_body',]

        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 border rounded-lg',
                'placeholder': 'Enter blog title'
            }),
            'category': forms.Select(attrs={
                'class': 'w-full px-3 py-2 border rounded-lg'
            }),
            'featured_image': forms.FileInput(attrs={
                'class': 'w-full px-3 py-2 border rounded-lg'
            }),
            'short_description': forms.Textarea(attrs={
                'class': 'w-full px-3 py-2 border rounded-lg',
                'rows': 3,
                'placeholder': 'Short description'
            }),
            'blog_body': forms.Textarea(attrs={
                'class': 'w-full px-3 py-2 border rounded-lg',
                'rows': 6,
                'placeholder': 'Write your blog...'
            }),
        }
