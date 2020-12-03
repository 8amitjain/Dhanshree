from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.views.generic.list import ListView
from django.template.defaultfilters import slugify
from django.shortcuts import redirect
from django.core.mail import EmailMessage
from django.conf import settings
from django.views.generic import TemplateView
from products.models import (
    Product, Category, ParentCategory
)
from products.filters import ProductFilter
from home.models import NewsLetter, Contact
from products.models import ProductContact

from .forms import SendBulkMailForm
from .filters import CategoryFilter, ParentCategoryFilter, ContactFilter, ProductContactFilter

from datetime import datetime, timedelta, time

today = datetime.now().date()
yesterday = today + timedelta(-1)


class AnalyticsView(UserPassesTestMixin, TemplateView):
    template_name = "analytics/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        product_contact = ProductContact.objects.all().count
        contact = Contact.objects.all().count
        product_contact_toady = ProductContact.objects.filter(date__gte=yesterday).count
        contact_toady = Contact.objects.filter(date__gte=yesterday).count

        context['product_contact_today'] = product_contact_toady
        context['contact_today'] = contact_toady
        context['product_contact_count'] = product_contact
        context['contact_count'] = contact
        return context

    def test_func(self):
        return self.request.user.is_staff is True


class AdminProductListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Product
    paginate_by = 4
    template_name = "analytics/product_list_admin.html"

    # queryset = Product.objects.filter(is_active=True)
    # Template name product_list.html
    # object_list variable name

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_query = Product.objects.all()
        product_filter = ProductFilter(self.request.GET, queryset=current_query)

        if len(product_filter.qs) != len(current_query):
            context['filter'] = product_filter
            context['object_list'] = product_filter.qs
            if len(product_filter.qs) < self.paginate_by:
                context['is_paginated'] = False
        return context

    def test_func(self):  # Giving only staff the permission to add Category
        return self.request.user.is_staff is True


# Add Products
class AdminProductAddView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Product
    fields = ['category', 'title', 'price', 'discount_price', 'label', 'short_description', 'description',
              'image_main', 'image_2', 'image_3', 'image_4', 'image_5', 'is_active']
    template_name = "analytics/product_add_update_admin.html"

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
class AdminProductUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    fields = ['category', 'title', 'price', 'discount_price', 'label', 'short_description', 'description',
              'image_main', 'image_2', 'image_3', 'image_4', 'image_5', 'is_active']
    template_name = "analytics/product_add_update_admin.html"
    # template name product_form
    # TODO Pass form button and heading data

    def test_func(self):  # Giving only staff the permission to add Category
        return self.request.user.is_staff is True


# Delete Products
class AdminProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    fields = ['category', 'title', 'price', 'discount_price', 'label', 'short_description', 'description',
              'image_main', 'image_2', 'image_3', 'image_4', 'image_5', 'is_active']
    success_url = '/'
    template_name = "analytics/product_confirm_delete.html"

    # template name product_confirm_delete.html
    # TODO display name in template of Product which is deleted
    # TODO Pass form button and heading data

    def test_func(self):  # Giving only staff the permission to add Category
        return self.request.user.is_staff is True


# Category
# Show all Category
class AdminCategoryListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Category
    paginate_by = 4
    # Template name category_list_admin.html
    # object_list variable name
    template_name = "analytics/category_list_admin.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_query = Category.objects.all()
        category_filter = CategoryFilter(self.request.GET, queryset=current_query)
        context['filter'] = category_filter
        if len(category_filter.qs) != len(current_query):
            context['object_list'] = category_filter.qs
            if len(category_filter.qs) < self.paginate_by:
                context['is_paginated'] = False
        return context

    def test_func(self):  # Giving only staff the permission to add Category
        return self.request.user.is_staff is True


# Add Category
class AdminCategoryAddView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Category
    fields = ['title', 'parent_category', 'description', 'image']
    template_name = "analytics/category_add_update_admin.html"

    # template name category_form

    def form_valid(self, form):
        form.instance.slug = slugify(form.instance.title)
        return super().form_valid(form)
    # TODO Pass form button and heading data

    def test_func(self):  # Giving only staff the permission to add Category
        return self.request.user.is_staff is True


# Update Category
class AdminCategoryUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Category
    fields = ['title', 'parent_category', 'description', 'image']
    template_name = "analytics/category_add_update_admin.html"

    # template name category_form
    # TODO Pass form button and heading data

    def test_func(self):  # Giving only staff the permission to add Category
        return self.request.user.is_staff is True


# Delete Category
class AdminCategoryDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Category
    fields = ['title', 'parent_category', 'description', 'image']
    success_url = '/'
    template_name = "analytics/category_confirm_delete.html"
    # template name category_confirm_delete.html
    # TODO Pass form button and heading data

    def test_func(self):  # Giving only staff the permission to add Category
        return self.request.user.is_staff is True


# Show all ParentCategory
class AdminParentCategoryListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = ParentCategory
    paginate_by = 4
    # Template name category_list_admin.html
    # object_list variable name
    template_name = "analytics/parent_category_list_admin.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_query = ParentCategory.objects.all()
        category_filter = ParentCategoryFilter(self.request.GET, queryset=current_query)
        context['filter'] = category_filter
        if len(category_filter.qs) != len(current_query):
            context['object_list'] = category_filter.qs
            if len(category_filter.qs) < self.paginate_by:
                context['is_paginated'] = False
        return context

    def test_func(self):  # Giving only staff the permission to add Category
        return self.request.user.is_staff is True


# Add Category
class AdminParentCategoryAddView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = ParentCategory
    fields = ['title', 'description', 'image']
    template_name = "analytics/parent_category_add_update_admin.html"

    # template name category_form

    def form_valid(self, form):
        form.instance.slug = slugify(form.instance.title)
        return super().form_valid(form)
    # TODO Pass form button and heading data

    def test_func(self):  # Giving only staff the permission to add Category
        return self.request.user.is_staff is True


# Update Category
class AdminParentCategoryUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = ParentCategory
    fields = ['title', 'description', 'image']
    template_name = "analytics/parent_category_add_update_admin.html"

    # template name category_form
    # TODO Pass form button and heading data

    def test_func(self):  # Giving only staff the permission to add Category
        return self.request.user.is_staff is True


# Delete Category
class AdminParentCategoryDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = ParentCategory
    fields = ['title', 'description', 'image']
    success_url = '/'
    template_name = "analytics/parent_category_confirm_delete.html"
    # template name category_confirm_delete.html
    # TODO Pass form button and heading data

    def test_func(self):  # Giving only staff the permission to add Category
        return self.request.user.is_staff is True


# SEND BULK MAIL
class SendMail(FormView):
    form_class = SendBulkMailForm
    template_name = 'analytics/send_bulk_mail.html'
    success_url = '/'

    def form_valid(self, form):
        form = form.cleaned_data
        email_subject = form['title']
        email_body = form['body']
        email = NewsLetter.objects.all()
        email = [e.email for e in email]

        email = EmailMessage(
            email_subject,
            email_body,
            settings.AUTH_USER_MODEL,
            email,
        )
        email.content_subtype = "html"
        email.send(fail_silently=False)
        return redirect('admin-dashboard')


# Show all ProductContact
class AdminProductContactListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = ProductContact
    paginate_by = 4
    # Template name category_list_admin.html
    # object_list variable name
    template_name = "analytics/product_contact_list_admin.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_query = ProductContact.objects.all()
        category_filter = ProductContactFilter(self.request.GET, queryset=current_query)
        context['filter'] = category_filter
        if len(category_filter.qs) != len(current_query):
            context['object_list'] = category_filter.qs
            if len(category_filter.qs) < self.paginate_by:
                context['is_paginated'] = False
        return context

    def test_func(self):  # Giving only staff the permission to add Category
        return self.request.user.is_staff is True


class AdminProductContactUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = ProductContact
    fields = ['name', 'read']
    template_name = "analytics/product_contact_update_admin.html"

    # template name category_form
    # TODO Pass form button and heading data

    def test_func(self):  # Giving only staff the permission to add Category
        return self.request.user.is_staff is True


class AdminContactListView(LoginRequiredMixin, UserPassesTestMixin, ListView):
    model = Contact
    paginate_by = 4
    # Template name category_list_admin.html
    # object_list variable name
    template_name = "analytics/contact_list_admin.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        current_query = Contact.objects.all()
        category_filter = ContactFilter(self.request.GET, queryset=current_query)
        context['filter'] = category_filter
        if len(category_filter.qs) != len(current_query):
            context['object_list'] = category_filter.qs
            if len(category_filter.qs) < self.paginate_by:
                context['is_paginated'] = False
        return context

    def test_func(self):  # Giving only staff the permission to add Category
        return self.request.user.is_staff is True


class AdminContactUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Contact
    fields = ['name', 'read']
    template_name = "analytics/contact_update_admin.html"

    # template name category_form
    # TODO Pass form button and heading data

    def test_func(self):  # Giving only staff the permission to add Category
        return self.request.user.is_staff is True
