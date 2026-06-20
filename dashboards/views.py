from multiprocessing import context, resource_tracker

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.template.defaultfilters import slugify

from blogs.models import Category, Blog
from dashboards.forms import CategoryForms, BlogPostForms, AddUserForms


#if user not logged in then django will redirect user to login since we have passed login_url
# as params to login_required decorator
@login_required(login_url='login')
def dashboard(request):
    category_count = Category.objects.all().count()
    blogs_count = Blog.objects.all().count()

    context = {
        'category_count': category_count,
        'blogs_count' : blogs_count
    }
    return render(request,'dashboard/dashboard.html', context)


def categories(request):
    return render(request,'dashboard/categories.html')


def add_category(request):
    if request.method == 'POST':
        form = CategoryForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('categories')
    else:
        form = CategoryForms()

    context = {
        'form': form
    }
    return render(request,'dashboard/add_category.html', context)


def edit_category(request,pk):
    category = get_object_or_404(Category,pk=pk)
    if request.method == 'POST':
        form = CategoryForms(request.POST, instance=category)
        if form.is_valid():
            form.save()
            return redirect('categories')
    #this instance of the form is setting the value in the form of category
    form = CategoryForms(instance=category)
    context = {
        'form': form,
        'category': category
    }
    return render(request, 'dashboard/edit_category.html',context)


def delete_category(request,pk):
    category = get_object_or_404(Category,pk=pk)
    category.delete()
    return redirect('categories')


def posts(request):
    dashboard_posts = Blog.objects.all()

    context = {
        'posts': dashboard_posts
    }
    return render(request,'dashboard/posts.html',context)


def add_post(request):
    if request.method == 'POST':
        #In request.POST: We receive the data like: title, category, status, short_description, blog_body etc
        #But the image will be received in request.FILES filed
        form = BlogPostForms(request.POST, request.FILES)
        if form.is_valid():
            temp_post = form.save(commit=False) #temporarily saving the form data
            temp_post.author = request.user
            temp_post.save() #saving the post here because I have to use the newly created post Id(pk) in below line
            temp_post.slug = slugify(form.cleaned_data['title'] + '-'+str(temp_post.id))
            temp_post.save()
            return redirect('posts')
    else:
        form = BlogPostForms()

    context = {
        'form': form
    }
    return render(request,'dashboard/add_post.html', context)


def edit_post(request,pk):
    post = get_object_or_404(Blog,pk=pk)
    if request.method == 'POST':
        form = BlogPostForms(request.POST, request.FILES, instance=post)
        if form.is_valid():
            updated_post = form.save()
            title = form.cleaned_data['title'] + '-'+str(updated_post.id)
            #Need to generate the slug again
            updated_post.slug = slugify(title)
            updated_post.save()
            return redirect('posts')

    form = BlogPostForms(instance=post) #Populating data in the form to edit
    context = {
        'form': form,
        'post': post
    }
    return render(request,'dashboard/edit_post.html',context)


def delete_post(request,pk):
    post = get_object_or_404(Blog,pk=pk)
    post.delete()
    return redirect('posts')


def users(request):
    dashboard_users = User.objects.all()
    context = {
        'users': dashboard_users
    }
    return render(request,'dashboard/users.html', context)

def add_user(request):
    if request.method == 'POST':
        form = AddUserForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users')
        else:
            print(form.errors)

    form = AddUserForms()
    context = {
        'form': form
    }

    return render(request,'dashboard/add_user.html',context)