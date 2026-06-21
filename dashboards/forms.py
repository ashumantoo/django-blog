from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from blogs.models import Category, Blog


class CategoryForms(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'


class BlogPostForms(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('title','category','featured_image','short_description','blog_body','status','is_featured')


class AddUserForms(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email','first_name','last_name','is_active','is_staff','is_superuser','groups','user_permissions')

#To edit the user - We can not use the AddUserForms because it has been inherited from UserCreationForm, which has password
# and confirm passwrod field. These password field is not required for edit
class EditUserForms(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','email','first_name','last_name','is_active','is_staff','is_superuser','groups','user_permissions')