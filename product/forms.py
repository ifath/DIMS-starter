from django import forms
from .models import Category, Product


class CategoryCreateForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ["category_name", "details", "parent_id"]
        # fields = "__all__"


class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ["p_name", "country_of_origin", "brand", "p_details"]

        labels = {
            "p_name": "Product Name",
            "p_details": "Configuration"
        }

