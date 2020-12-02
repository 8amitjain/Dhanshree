from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

from . import views


urlpatterns = [
    path('', views.AnalyticsView.as_view(), name='admin-dashboard'),

    # Products
    path('product/list-admin/', views.AdminProductListView.as_view(), name='admin-product-list'),
    path('product/add/', views.AdminProductAddView.as_view(), name='admin-product-add'),
    path('product/update/<int:pk>/', views.AdminProductUpdateView.as_view(), name='admin-product-update'),
    path('product/delete/<int:pk>/', views.AdminProductDeleteView.as_view(), name='admin-product-delete'),

    # Category
    path('category/list-admin/', views.AdminCategoryListView.as_view(), name='admin-category-list'),
    path('category/add/', views.AdminCategoryAddView.as_view(), name='admin-product-category-add'),
    path('category/update/<int:pk>/', views.AdminCategoryUpdateView.as_view(), name='admin-product-category-update'),
    path('category/delete/<int:pk>/', views.AdminCategoryDeleteView.as_view(), name='admin-product-category-delete'),

    # Parent Category
    path('parent/category/list-admin/', views.AdminParentCategoryListView.as_view(), name='admin-parent-category-list'),
    path('parent/category/add/', views.AdminParentCategoryAddView.as_view(), name='admin-product-parent-category-add'),
    path('parent/category/update/<int:pk>/', views.AdminParentCategoryUpdateView.as_view(),
         name='admin-product-parent-category-update'),
    path('parent/category/delete/<int:pk>/', views.AdminParentCategoryDeleteView.as_view(),
         name='admin-product-parent-category-delete'),

    path('send/mail/', views.SendMail.as_view(), name='admin-send-mail'),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
