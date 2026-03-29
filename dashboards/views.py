from django.contrib.auth.decorators import login_required

from django.contrib.auth.decorators import permission_required

# dashboard to staff only
from django.contrib.admin.views.decorators import staff_member_required

from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from .form import BlogForm, CategoryForm, EditUserForm, UserForm
from blogs.models import Blog, Category

from django.contrib.auth.models import User


@login_required(login_url='login')
@staff_member_required(login_url='login')
def dashboard(request):
    return render(request, 'dashboard/dashboard.html')

# -----------------------------------------------------------------------------------
@login_required(login_url='login')
@permission_required('blogs.view_blog', raise_exception=True)
def blog(request):

    blog = Blog.objects.filter(author__is_staff=True)

    categorie = Category.objects.all()

    category_id = request.GET.get('category')
    status = request.GET.get('status')

    # Filter by category
    if category_id:
        blog = blog.filter(category_id=category_id)

    # Filter by status
    if status:
        blog = blog.filter(status=status)

    context={
        'blog': blog,
        'categorie': categorie,
    }
    return render(request, 'dashboard/blogboard.html', context)

@login_required(login_url='login')
@permission_required('blogs.view_blog', raise_exception=True)
def user_blog(request):

    blog = Blog.objects.filter(author__is_staff=False)

    categorie = Category.objects.all()

    category_id = request.GET.get('category')
    status = request.GET.get('status')

    # Filter by category
    if category_id:
        blog = blog.filter(category_id=category_id)

    # Filter by status
    if status:
        blog = blog.filter(status=status)

    context={
        'blog': blog,
        'categorie': categorie,
    }
    return render(request, 'dashboard/userblogboard.html', context)

@login_required(login_url='login')
@permission_required('blogs.add_blog', raise_exception=True)
def add_blog(request):
    form = BlogForm()

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES) #request.FILES for the images or files // because request.post take form field but when it come to img or files like pdf etc. we use request.FILES
        if form.is_valid():
            blog = form.save(commit=False)   # temporarily saving the form not in db because author is missing in form
            blog.author = request.user       # manually add: set logged-in user as author
            blog.save()                      # now save
            return redirect('blog')

    context = {
        'form': form,
    }
    return render(request, 'dashboard/add_blog.html', context)

@login_required(login_url='login')
@permission_required('blogs.change_blog', raise_exception=True)
def edit_blog(request, id):
    blog = get_object_or_404(Blog, id=id)

    if blog.author != request.user and not request.user.is_superuser:
        return HttpResponse("Not allowed", status=403)

    
    form = BlogForm(instance=blog)

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog) 
        if form.is_valid():
            form.save()                     
            return redirect('dashboard')

    context = {
        'form': form,
        'blog': blog,
    }
    return render(request, 'dashboard/edit_blog.html', context)

@login_required(login_url='login')
@permission_required('blogs.delete_blog', raise_exception=True)
def delete_blog(request, id):
    blog = get_object_or_404(Blog, id=id)
    blog.delete()
    return redirect('blog')

# -------------------------------------------------------------------------------------------
@login_required(login_url='login')
@permission_required('blogs.view_category', raise_exception=True)
def categorie(request):
    query = request.GET.get('q', '')  # Get search query from input

    if query:
        # Filter categories by search query
        categories = Category.objects.filter(category_name__icontains=query)
        if not categories.exists():
            message = "Category not present"
        else:
            message = None
    else:
        # If no search query, show all
        categories = Category.objects.all()
        message = None

    context = {
        'categories': categories,
        'message': message,
    }
    return render(request, 'dashboard/categorie.html', context)

@login_required(login_url='login')
@permission_required('blogs.add_category', raise_exception=True)
def add_category(request):
    form = CategoryForm()

    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categorie')
        
    context = {
        'form': form,
    }
    return render(request, 'dashboard/add_category.html', context)

@login_required(login_url='login')
@permission_required('blogs.delete_category', raise_exception=True)
def delete_category(request, id):
    category = get_object_or_404(Category, id=id)
    category.delete()
    return redirect('categorie')

@login_required(login_url='login')
@permission_required('blogs.change_category', raise_exception=True)
def edit_category(request, id):
    category = get_object_or_404(Category, id=id)
    form = CategoryForm(instance=category) # pre fill

    if request.method == 'POST':
        form = CategoryForm(request.POST, instance=category) # add instance if not it will create new row witn instance update on exiting row
        if form.is_valid():
            form.save()
            return redirect('categorie')
        
    context = {
        'form': form,
        'category': category,
    }
    return render(request, 'dashboard/edit_category.html', context)

# ---------------------------------------------------------------------------------------------
@login_required(login_url='login')
@permission_required('auth.view_user', raise_exception=True)
def user(request):
    users = User.objects.all() 
    context = {
        'users': users
    }
    return render(request, 'dashboard/userboard.html', context)

@login_required(login_url='login')
@permission_required('auth.add_user', raise_exception=True)
def add_user(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()  
            return redirect('user')
        
    context = {
        'form': form,
    }
    return render(request, 'dashboard/add_user.html', context)

@login_required(login_url='login')
@permission_required('auth.change_user', raise_exception=True)
def edit_user(request, id):
    user = get_object_or_404(User, id=id)
    form = EditUserForm(instance=user)

    if request.method == 'POST':
        form = EditUserForm(request.POST, instance=user) 
        if form.is_valid():
            form.save()
            return redirect('user')
        
    context = {
        'form':form,
        'user': user
    }
    return render (request, 'dashboard/edit_user.html', context)

@login_required(login_url='login')
@permission_required('auth.delete_user', raise_exception=True)
def delete_user(request, id):
    user = get_object_or_404(User, id=id)
    user.delete()
    return redirect('user')