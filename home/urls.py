from django.urls import path
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', TemplateView.as_view(template_name="home/home.html"), name='home'),
    path('product/', TemplateView.as_view(template_name="home/product.html"), name='product'),
    path('productdetail/', TemplateView.as_view(template_name="home/product_detail.html"), name='product-detail'),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
