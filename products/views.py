from django.views.generic.list import ListView
from django.views.generic import View
from django.shortcuts import render
from django.http import HttpResponseRedirect

from .filters import ProductFilter
from .models import (
    Product
)
from .forms import ProductForm


# Products
# Show all Products
class ProductListView(ListView):
    model = Product
    paginate_by = 4

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_query = Product.objects.all()
        product_filter = ProductFilter(self.request.GET, queryset=current_query)
        context['filter'] = product_filter
        if len(product_filter.qs) != len(current_query):
            context['object_list'] = product_filter.qs
            if len(product_filter.qs) < self.paginate_by:
                context['is_paginated'] = False
        return context


class ProductDetailView(View):
    def get(self, *args, **kwargs):
        context = {}
        product = Product.objects.get(id=self.kwargs.get('pk'))
        price = product.price
        discount_price = product.discount_price
        context['object'] = product
        context['discount_percent'] = int(100 - ((discount_price / price) * 100))
        context['form'] = ProductForm()
        return render(self.request, 'products/product_detail.html', context)

    def post(self, *args, **kwargs):
        form = ProductForm(self.request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            product = Product.objects.get(id=self.kwargs.get('pk'))
            form.product = product
            form.save()
        return HttpResponseRedirect(self.request.META.get('HTTP_REFERER'))
