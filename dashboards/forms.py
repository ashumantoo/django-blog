from django import forms

from blogs.models import Category


class CategoryForms(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'