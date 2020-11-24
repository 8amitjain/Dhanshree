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


class Category(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    image = models.ImageField(upload_to='category', null=True, blank=True)  # image of slide ...
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):  # Redirect to this link after adding category , kwargs={'slug': self.slug })
        return reverse("product-category-list-view")


# TODO Add Variation type
# TODO ADD Qty Type
# TODO ADD a filed maintain stock if true show stock nos opt
# TODO if one image is added show option to add more image till 5

class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # item_ref_number = models.CharField(unique=True, default='IRN-100000', max_length=15)

    title = models.CharField(max_length=200, unique=True)
    price = models.FloatField()
    discount_price = models.FloatField(blank=True, null=True)
    label = models.CharField(choices=LABEL_CHOICES, max_length=11, null=True, blank=True,
                             help_text="Item is of Sale, New Arrival etc or leave it blank for no label. \
                                        (Label will be displayed over a item.)")
    slug = models.SlugField(unique=True)

    stock_no = models.IntegerField()  # number of products in stock
    short_description = models.TextField(help_text='To describe product in short', null=True, blank=True)
    description = models.TextField(help_text='Overview product', null=True, blank=True)

    image_main = models.ImageField(upload_to='products', null=True, blank=True)
    image_2 = models.ImageField(upload_to='products', null=True, blank=True)
    image_3 = models.ImageField(upload_to='products', null=True, blank=True)
    image_4 = models.ImageField(upload_to='products', null=True, blank=True)
    image_5 = models.ImageField(upload_to='products', null=True, blank=True)

    is_active = models.BooleanField(default=True)
    trending = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):  # Redirect to this link after adding product
        return reverse("product-list-view")

