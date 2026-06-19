from django.contrib import admin

from blogs.models import Category, Blog

class BlogAdmin(admin.ModelAdmin):
    # To generate/pre populate the slug as we type blog title from admin panel
    prepopulated_fields = {'slug':('title',)}
    #This will display the following column on the Blog table inside the admin paner
    list_display = ('title','category','author','status','is_featured')
    #to search on the table - category is a foreign key thus we need to write category__category_name
    search_fields = ('id','title','category__category_name','status')
    #to make a field editable on the table itself
    list_editable = ('is_featured',)

# Register your models here.
admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)