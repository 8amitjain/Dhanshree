import django_filters
from django import forms

from .models import Product, Category, ProductContact


class ProductFilter(django_filters.FilterSet):
    discount_price = django_filters.RangeFilter(field_name="discount_price")
    note = django_filters.CharFilter(field_name='title', lookup_expr='icontains')
    category = django_filters.ModelMultipleChoiceFilter(queryset=Category.objects.all(),
                                                        widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Product
        fields = ['category']

