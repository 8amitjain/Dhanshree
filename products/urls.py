from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

urlpatterns = [

    # Products
    path('list/', views.ProductListView.as_view(), name='product-list-view'),
    path('detail/<int:pk>/', views.ProductDetailView.as_view(), name='product-detail-view'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

