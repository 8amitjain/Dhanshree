from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views

# TODO Display a page show products
# TODO Display a page show category

urlpatterns = [
    # Admin
    # Category
    path('category/', views.CategoryListView.as_view(), name='product-category-list-view'),
    path('category/add/', views.CategoryAddView.as_view(), name='product-category-add'),
    path('category/update/<int:pk>/', views.CategoryUpdateView.as_view(), name='product-category-update'),
    path('category/delete/<int:pk>/', views.CategoryDeleteView.as_view(), name='product-category-delete'),

    # Products
    path('list/', views.ProductListView.as_view(), name='product-list-view'),
    path('detail/<int:pk>/', views.ProductDetailView.as_view(), name='product-detail-view'),
    path('add/', views.ProductAddView.as_view(), name='product-add'),
    path('update/<int:pk>/', views.ProductUpdateView.as_view(), name='product-update'),
    path('delete/<int:pk>/', views.ProductDeleteView.as_view(), name='product-delete'),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

