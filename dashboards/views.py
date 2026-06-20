from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from blogs.models import Category, Blog
from dashboards.forms import CategoryForms


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