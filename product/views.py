from django.shortcuts import render, redirect, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, FormView
from django.contrib import messages

from .models import Category,Product
from .forms import CategoryCreateForm, ProductCreateForm


def category_create(request):
    if request.method == 'POST':
        category_name = request.POST.get('category_name', '')
        details = request.POST.get('details', '')
        parent_id = request.POST.get('parent_id', '')

        if parent_id != '':
            parent_object = Category.objects.get(id=parent_id)
        else:
            parent_object = default = None

        current_user = request.user

        category_obj = Category(category_name=category_name, details=details, parent_id=parent_object,
                                created_by=current_user, active_status=1)
        category_obj.save()

        categories = Category.objects.order_by('id').all()
        context = {'categories': categories}
        
        return render(request, 'product/category_list.html', context)


    else:
        context = {}
        context['form'] = CategoryCreateForm()
        # print(context['form'].parent_id)

        return render(request, 'product/category_entry_form.html', context)

def category_list(request):
    categories = Category.objects.order_by('id').all()
    context = {'categories': categories}
    return render(request, 'product/category_list.html', context)


class ProductCreateView(CreateView):
    template_name = 'product/product-create.html'
    form_class = ProductCreateForm

    # def get_initial(self, *args, **kwargs):
    #     initial = super(ProductCreateView, self).get_initial(**kwargs)
    #     initial['category_name'] = 'My Product'
    #     return initial

    def post(self, request, *args, **kwargs):
        form = ProductCreateForm(request.POST)
        if form.is_valid():
            product = form.save()
            product.created_by = request.user
            product.save()
            # return HttpResponseRedirect(reverse_lazy('products:detail', args=[product.id]))
            messages.info(request, 'product inserted')
        return render(request, 'product/product-create.html', {'form': form})



