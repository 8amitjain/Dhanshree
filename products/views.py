from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.template.defaultfilters import slugify
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from .models import (
    Category, Product
)

# TODO only staff can change add and update data
# TODO Set delete success url to product displace page
# TODO Create a page to display Current Products and Category


# Category
# Show all Category
class CategoryListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Category
    # Template name category_list.html
    # object_list variable name

    def test_func(self):  # Giving only staff the permission to add Category
        return self.request.user.is_staff is True


# Add Category
class CategoryAddView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Category
    fields = ['title', 'description', 'image']
    # template name category_form

    def form_valid(self, form):
        form.instance.slug = slugify(form.instance.title)
        return super().form_valid(form)
    # TODO Pass form button and heading data

    def test_func(self):  # Giving only staff the permission to add Category
        return self.request.user.is_staff is True


# Update Category
class CategoryUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Category
    fields = ['title', 'description', 'image']
    # template name category_form
    # TODO Pass form button and heading data

    def test_func(self):  # Giving only staff the permission to add Category
        return self.request.user.is_staff is True


# Delete Category
class CategoryDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Category
    fields = ['title', 'description', 'image']
    success_url = '/'
    # template name category_confirm_delete.html
    # TODO Pass form button and heading data

    def test_func(self):  # Giving only staff the permission to add Category
        return self.request.user.is_staff is True


# Products
# Show all Products
class ProductListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Product
    # queryset = Product.objects.filter(is_active=True)
    # Template name product_list.html
    # object_list variable name

    def test_func(self):  # Giving only staff the permission to add Category
        return self.request.user.is_staff is True


# Detail Product
class ProductDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Product
    # Template name product_detail.html
    # object variable name

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviewed'] = "False"
        for review in self.object.review.all():
            if review.user == self.request.user:
                context['reviewed'] = "True"
        return context

    def test_func(self):  # Giving only staff the permission to add Category
        return self.request.user.is_staff is True


# Add Products
class ProductAddView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Product
    fields = ['category', 'title', 'price', 'discount_price', 'label', 'stock_no', 'short_description', 'description',
              'image_main', 'image_2', 'image_3', 'image_4', 'image_5', 'is_active']
    # template name product_form

    def form_valid(self, form):
        product = form.save(commit=False)
        product.slug = slugify(product.title)
        product.save()
        product.item_ref_number = f"PRN-{100000 + int(product.id)}"
        product.save()
        return super().form_valid(form)
    # TODO Pass form button and heading data

    def test_func(self):  # Giving only staff the permission to add Category
        return self.request.user.is_staff is True


# Update Products
class ProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    fields = ['category', 'title', 'price', 'discount_price', 'label', 'stock_no', 'short_description', 'description',
              'image_main', 'image_2', 'image_3', 'image_4', 'image_5', 'is_active']
    # template name product_form
    # TODO Pass form button and heading data

    def test_func(self):  # Giving only staff the permission to add Category
        return self.request.user.is_staff is True


# Delete Products
class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    fields = ['category', 'title', 'price', 'discount_price', 'label', 'stock_no', 'short_description', 'description',
              'image_main', 'image_2', 'image_3', 'image_4', 'image_5', 'is_active']
    success_url = '/'
    # template name product_confirm_delete.html
    # TODO display name in template of Product which is deleted
    # TODO Pass form button and heading data

    def test_func(self):  # Giving only staff the permission to add Category
        return self.request.user.is_staff is True


