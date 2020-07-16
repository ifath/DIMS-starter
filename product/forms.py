from django import forms
from .models import Category

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["category_name", "details", "parent_id"]
        # fields = "__all__"
