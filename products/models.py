from django.db import models
from django.shortcuts import reverse
from django.utils import timezone


LABEL_CHOICES = (
    ('Sale', 'Sale'),
    ('New Arrival', 'New Arrival'),
    ('Trending', 'Trending'),
    ('Top Selling', 'Top Selling'),
    ('Popular', 'Popular'),
)


class ParentCategory(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(unique=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='parent_category', null=True, blank=True)  # image of slide ...
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):  # Redirect to this link after adding category , kwargs={'slug': self.slug })
        return reverse("admin-parent-category-list")


class Category(models.Model):
    parent_category = models.ForeignKey(ParentCategory, on_delete=models.CASCADE)

    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(unique=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='category', null=True, blank=True)  # image of slide ...
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):  # Redirect to this link after adding category , kwargs={'slug': self.slug })
        return reverse("admin-category-list")


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    title = models.CharField(max_length=200, unique=True)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    discount_price = models.DecimalField(max_digits=20, decimal_places=2)

    label = models.CharField(choices=LABEL_CHOICES, max_length=11, null=True, blank=True,
                             help_text="Item is of Sale, New Arrival etc or leave it blank for no label. \
                                        (Label will be displayed over a item.)")
    slug = models.SlugField(unique=True)

    short_description = models.TextField(help_text='To describe product in short', null=True, blank=True)
    description = models.TextField(help_text='Overview product', null=True, blank=True)

    image_main = models.ImageField(upload_to='products', null=True, blank=True)
    image_2 = models.ImageField(upload_to='products', null=True, blank=True)
    image_3 = models.ImageField(upload_to='products', null=True, blank=True)
    image_4 = models.ImageField(upload_to='products', null=True, blank=True)
    image_5 = models.ImageField(upload_to='products', null=True, blank=True)

    is_active = models.BooleanField(default=True)
    trending = models.BooleanField(default=False)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'products_product'
        ordering = ['title']

    def __str__(self):
        return self.title

    def get_absolute_url(self):  # Redirect to this link after adding product
        return reverse("admin-product-list")


class ProductContact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(null=True, blank=True)
    mobile = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    date = models.DateField(default=timezone.now)
    read = models.BooleanField(default=False)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"{self.name}_{self.mobile}"

    def get_absolute_url(self):  # Redirect to this link after adding review
        return reverse("admin-product-contact")


# class VariationManger(models.Manager):
#     def all(self):
#         return super(VariationManger, self).filter(active=True)
#
#     def sizes(self):
#         return self.all().filter(category='size')
#
#     def colors(self):
#         return self.all().filter(category='color')


# VARIATION_CATEGORIES = (
#     ('size', 'size'),
#     ('color', 'color'),
# )
#
#
# class Variation(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     category = models.CharField(choices=VARIATION_CATEGORIES, max_length=20, default='size')
#     title = models.CharField(max_length=200)
#     color_code = models.CharField(max_length=200, null=True, blank=True)
#     price = models.DecimalField(max_digits=20, decimal_places=2)
#     discount_price = models.DecimalField(max_digits=20, decimal_places=2)
#     active = models.BooleanField(default=True)
#
#     objects = VariationManger()
#
#     class Meta:
#         unique_together = ('title', 'product',)
#
#     def __str__(self):
#         return f'{self.product.title}_{self.title}_variation'




