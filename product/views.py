from django.shortcuts import render, redirect
from .forms import CategoryForm

from .models import Category


def showform(request):
    if request.method == 'POST':
        category_name = request.POST.get('category_name', '')
        details = request.POST.get('details', '')
        parent_id = request.POST.get('parent_id', '')
        parent_object = Category.objects.get(id=parent_id)

        category_obj = Category(category_name=category_name, details=details, parent_id=parent_object)
        category_obj.save()

        categories = Category.objects.order_by('id').all()
        context = {'categories': categories}
        return render(request, 'product/category_list.html', context)
        return render(request, 'product/category_entry_form.html', context)

    else:
        context = {}
        context['form'] = CategoryForm()

        return render(request, 'product/category_entry_form.html', context)

def category_list(request):
    categories = Category.objects.order_by('id').all()
    context = {'categories': categories}
    return render(request, 'product/category_list.html', context)



