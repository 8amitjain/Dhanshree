import django_filters

from products.models import Category, ProductContact
from home.models import Contact


class CategoryFilter(django_filters.FilterSet):
    note = django_filters.CharFilter(field_name='title', lookup_expr='icontains')

    class Meta:
        model = Category
        fields = ['is_active']


class ParentCategoryFilter(django_filters.FilterSet):
    note = django_filters.CharFilter(field_name='title', lookup_expr='icontains')

    class Meta:
        model = Category
        fields = ['is_active']


class ContactFilter(django_filters.FilterSet):
    start_date = django_filters.DateFilter(field_name="date", lookup_expr='gte')
    end_date = django_filters.DateFilter(field_name="date", lookup_expr='lte')

    class Meta:
        model = Contact
        fields = ['read']


class ProductContactFilter(django_filters.FilterSet):
    start_date = django_filters.DateFilter(field_name="date", lookup_expr='gte')
    end_date = django_filters.DateFilter(field_name="date", lookup_expr='lte')

    class Meta:
        model = ProductContact
        fields = ['read']
