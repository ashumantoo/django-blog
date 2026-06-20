from blogs.models import Category

#context processors in django is something which allows us to pass some value which will be
#accessible inside all the html pages
def get_categories(request):
    categories = Category.objects.all()
    return dict(categories=categories)