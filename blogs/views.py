from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

from django.template.defaultfilters import title

from blogs.models import Blog, Category


# Create your views here.
def posts_by_category(request,category_id):
    #fetch the post that belongs to the category_id
    # posts = Blog.objects.filter(status='Published', category_id=category_id)
    #this will also work and upper one is also work
    # , (comma) works as and operator
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

def blogs(request, slug):
    blog = get_object_or_404(Blog, slug=slug, status='Published')
    context = {
        'blog':blog
    }
    return render(request,'blog.html', context)


def search(request):
    keyword = request.GET.get('keyword')
    # searched_blogs = Blog.objects.filter(title__icontains=keyword)
    # Q from django model - used to do the complex query on database - here I want to fetch the blogs which can be matched
    # with the title, short description or even with the body of the blog
    searched_blogs = Blog.objects.filter(Q(title__icontains=keyword)
                                         | Q(short_description__icontains=keyword)
                                         | Q(blog_body__icontains=keyword),
                                         status='Published')
    context = {
        'searched_blogs': searched_blogs,
        'keyword':keyword
    }
    return render(request,'search.html', context)