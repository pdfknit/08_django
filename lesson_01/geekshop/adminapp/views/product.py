from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView
from mainapp.models import Product, ProductCategory
from adminapp.forms import ProductCreateAdminForm
from django.utils.decorators import method_decorator
from adminapp.utils import superuser_required_decorator


class ProductCreateView(CreateView):
    model = Product
    template_name = 'adminapp/product_edit.html'
    fields = '__all__'
    success_url = ...

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.get_category()
        return context

    def get_success_url(self):
        return reverse('admin:products', kwargs=self.kwargs)

    def get_initial(self):
        return {
            'category': self.get_category()
        }

    def get_category(self):
        return ProductCategory.objects.get(pk=self.kwargs['pk'])

    @method_decorator(superuser_required_decorator)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


def product_read(request):
    pass


def products(request, pk):
    category = get_object_or_404(ProductCategory, pk=pk)
    products = Product.objects.filter(category_id=category).order_by('id')

    return render(request, 'adminapp/products.html', context={
        'title': 'Продукты',
        'category': category,
        'objects': products,
    })


def product_update(request):
    pass


def product_delete(request, pk):
    pass
