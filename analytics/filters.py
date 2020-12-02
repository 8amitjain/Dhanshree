import django_filters

from products.models import Category


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
