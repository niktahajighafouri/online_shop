
# Create your views here.
from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView, ListView, DetailView
from django.contrib import messages
from django.urls import reverse_lazy
from .models import Category, Product
from permissions import IsAdminUserMixing
# from orders.forms import CartAddForm

# Create your views here.
class ProductView(View):
    template_name = 'products/products.html'

    def get(self, request, category_slug=None):
        products = Product.objects.filter(available=True)
        categories = Category.objects.filter(is_sub=False)

        if category_slug:
            category = Category.objects.get(slug=category_slug)
            products = products.filter(category=category)
        context = {
            'products': products,
            'categories': categories,
        }
        return render(request, self.template_name, context)


class ProductDetailView(DetailView):
    template_name = 'products/product_details.html'
    # form_class = CartAddForm
    model = Product
    context_object_name = 'product'

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['form'] = self.form_class()
    #     return context


class AdminHomeView(IsAdminUserMixing, ListView):
    template_name = 'products/bucket.html'
    model = Product
    context_object_name = 'objects'


class AdminProductDelete(IsAdminUserMixing, DetailView):
    model = Product
    success_url = reverse_lazy('products:bucket')
    template_name = 'products/delete.html'
