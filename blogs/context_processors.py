from assignments.models import SocialLink
from blogs.models import Category

#context processors in django is something which allows us to pass some value which will be
#accessible inside all the html pages
def get_categories(request):
    categories = Category.objects.all()
    return dict(categories=categories)

def get_social_links(request):
    social_links = SocialLink.objects.all()
    return dict(social_links=social_links)