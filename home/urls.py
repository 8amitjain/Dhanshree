from django.urls import path
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings

from .views import NewsLetterCreateView, ContactView

urlpatterns = [
    path('', TemplateView.as_view(template_name='home/home.html'), name='home'),
    path('about/', TemplateView.as_view(template_name='home/about.html'), name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('newsletter/', NewsLetterCreateView.as_view(), name='news-letter'),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
