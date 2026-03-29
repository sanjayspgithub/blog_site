
from django import forms
from blogs.models import Category, Blog

from django.contrib.auth.models import User




class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['category_name']  
        widgets = {
            'category_name': forms.TextInput(attrs={
                'class': 'w-full px-4 py-2 border border-black rounded-lg focus:outline-none focus:border-black',
                'placeholder': 'Enter category name'
            })
        }

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = [  'title',
                    'category',
                    'featured_image',
                    'short_description',
                    'blog_body',
                    'status', ]

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
            'status': forms.Select(attrs={
                'class': 'w-full px-3 py-2 border rounded-lg'
            }),
        }


class UserForm(forms.ModelForm):

    email = forms.EmailField(required=True,
            widget= forms.EmailInput(attrs={
                'class': 'w-full px-3 py-2 border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-[#0B1C33]',
                'placeholder': 'Enter email'
            }))
    
    password = forms.CharField(required=True,
    widget=forms.PasswordInput(attrs={
        'id': 'passwordField', 
        'class': 'w-full px-3 py-2 border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-[#0B1C33]',
        'placeholder': 'Enter password'
    }))

    class Meta: 

        model = User
        fields = [  'username', 
                    'first_name',
                    'last_name',
                    'email',
                    'is_active',
                    'is_staff',
                    'groups',
                    'user_permissions',
                    'password',
                    ]

        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-[#0B1C33]',
                'placeholder': 'Enter username'
            }),

            'first_name': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-[#0B1C33]',
                'placeholder': 'Enter first name'
            }),

            'last_name': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-[#0B1C33]',
                'placeholder': 'Enter last name'
            }),

            'is_active': forms.CheckboxInput(attrs={
                'class': 'h-4 w-4 text-blue-600 border-gray-300 rounded focus:ring-[#0B1C33]'
            }),

            'is_staff': forms.CheckboxInput(attrs={
                'class': 'h-4 w-4 text-blue-600 border-gray-300 rounded focus:ring-[#0B1C33]'
            }),

            'groups': forms.SelectMultiple(attrs={
                'class': 'w-full px-3 py-2 border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-[#0B1C33]'
            }),

            'user_permissions': forms.SelectMultiple(attrs={
                'class': 'w-full px-3 py-2 border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-[#0B1C33]'
            }),

        }

    def save(self, commit=True):
        user = super().save(commit=False)

        # hash password
        user.set_password(self.cleaned_data['password'])

        if commit:
            user.save()
            self.save_m2m()

        return user
    





class EditUserForm(forms.ModelForm):

    email = forms.EmailField(required=True,
            widget= forms.EmailInput(attrs={
                'class': 'w-full px-3 py-2 border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-[#0B1C33]',
                'placeholder': 'Enter email'
            }))
    
    password = forms.CharField(required=False,
    widget=forms.PasswordInput(attrs={
        'id': 'passwordField', 
        'class': 'w-full px-3 py-2 border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-[#0B1C33]',
        'placeholder': 'Enter password'
    }))

    class Meta: 

        model = User
        fields = [  'username', 
                    'first_name',
                    'last_name',
                    'email',
                    'is_active',
                    'is_staff',
                    'groups',
                    'user_permissions',
                    'password',
                    ]

        widgets = {
            'username': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-[#0B1C33]',
                'placeholder': 'Enter username'
            }),

            'first_name': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-[#0B1C33]',
                'placeholder': 'Enter first name'
            }),

            'last_name': forms.TextInput(attrs={
                'class': 'w-full px-3 py-2 border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-[#0B1C33]',
                'placeholder': 'Enter last name'
            }),

            'is_active': forms.CheckboxInput(attrs={
                'class': 'h-4 w-4 text-blue-600 border-gray-300 rounded focus:ring-[#0B1C33]'
            }),

            'is_staff': forms.CheckboxInput(attrs={
                'class': 'h-4 w-4 text-blue-600 border-gray-300 rounded focus:ring-[#0B1C33]'
            }),

            'groups': forms.SelectMultiple(attrs={
                'class': 'w-full px-3 py-2 border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-[#0B1C33]'
            }),

            'user_permissions': forms.SelectMultiple(attrs={
                'class': 'w-full px-3 py-2 border border-slate-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-[#0B1C33]'
            }),

        }

    def save(self, commit=True):
        user = super().save(commit=False)

        password = self.cleaned_data.get('password')

        # Only update if new password entered
        if password:
            user.set_password(password)

        if commit:
            user.save()
            self.save_m2m()

        return user