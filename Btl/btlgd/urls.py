from django.urls import path
from btlgd.views import index, product, description, contact
from django.conf.urls.static import static
from Btl import settings


urlpatterns = [
    path('', index, name='home'),
    path('product', product, name='product'),
    path('description', description, name='des'),
    path('contact', contact, name='contact'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)