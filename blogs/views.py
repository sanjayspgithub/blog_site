from django.contrib.auth.decorators import login_required

from django.shortcuts import get_object_or_404, redirect, render

from .form import UserAddBlogForm
from .models import Blog, Category, Comment
from django.db.models import Q


def category_posts(request, id):

    # try:
    #     category_name = Category.objects.get(id=id)
    #     # If xyz is not present in category then it will redirect it to home page 
    # except:
    #     return redirect('home')

    # to show the error page 
    category_name = get_object_or_404(Category, id=id)
    posts = Blog.objects.filter(status='published', category_id=id)

    context = {
        'posts': posts,
        'category_name' : category_name,
        'active_category': id
    }

    return render(request, 'post.html', context)


def sblogs(request, slug):
    single_blog = get_object_or_404(Blog, slug=slug, status='published')

    # Handle comment submission
    if request.method == "POST":
        comment_text = request.POST.get('comment')

        if comment_text:
            Comment.objects.create(
                blog=single_blog,              # link to blog
                user=request.user,             # logged-in user
                comment=comment_text          # comment text
            )
            return redirect('sblogs', slug=slug)

    # show comments
    comments = Comment.objects.filter(blog=single_blog)
    comment_count = comments.count

    context = {
        'single_blog':single_blog,
        'comments':comments,
        'comment_count':comment_count,
    }
    return render(request, 'blogs.html', context)


def search(request):
    keyword = request.GET.get('keyword')

    blog = Blog.objects.filter(
            Q(title__icontains=keyword) |
            Q(short_description__icontains=keyword) |
            Q(blog_body__icontains=keyword),
            status='published')

    context = {
        'blog': blog,
        'keyword': keyword
    }
    return render(request, 'search.html', context)


@login_required(login_url='login')
def add_b(request):
    blogs = Blog.objects.filter(author=request.user)

    status = request.GET.get('status')
    if status is not None and status != "":
        blogs = blogs.filter(status=status)

    context = {'blogs': blogs,
        'selected_status': status}
    return render(request, 'add_blog.html', context)

@login_required(login_url='login')
def add_blog_f(request):
    
    form = UserAddBlogForm()

    if request.method == 'POST':
        form = UserAddBlogForm(request.POST, request.FILES) 
        if form.is_valid():
            blog = form.save(commit=False) 
            blog.author = request.user 
            blog.status = 'pending'
            blog.save()                      
            return redirect('add_b')
        
    context = {
        'form':form
    }
    return render(request, 'add_blog_f.html', context)

@login_required(login_url='login')
def user_delete_blog(request, id):
    blog = get_object_or_404(Blog, id=id)
    blog.delete()
    return redirect('add_b')

@login_required(login_url='login')
def edit_blog_f(request, id):
    blog = get_object_or_404(Blog, id=id)
    form = UserAddBlogForm(instance=blog)

    if request.method == 'POST':
        form = UserAddBlogForm(request.POST, request.FILES, instance=blog) 
        if form.is_valid():
            blog.status = 'pending'
            form.save()                     
            return redirect('add_b')

    context = {
        'blog': blog,
        'form': form,
    }
    return render(request, 'edit_blog_f.html', context)

