from django.shortcuts import render, get_object_or_404, redirect

from blogs.models import Blog, Category


# Create your views here.
def posts_by_category(request,category_id):
    #fetch the post that belongs to the category_id
    # posts = Blog.objects.filter(status='Published', category_id=category_id)
    #this will also work and upper one is also work
    posts = Blog.objects.filter(status='Published', category=category_id)

    #Use if you want to show 404 error page
    category = get_object_or_404(Category, pk=category_id)

    #use try and except when you want to do some custom action if category does not exits
    # try:
    #     category = Category.objects.get(pk=category_id)
    # except:
    #     #Redirect to home
    #     return redirect('home')

    context = {
        'posts':posts,
        'category': category
    }
    return render(request, 'posts_by_category.html',context)