from django.urls import path, include
from .views import *

urlpatterns = [
   path('',homepage,name ='index'),
   path('about', about, name = 'about'),
   path('services', service, name = 'service'),
   path('contact', contact, name = 'contact'),
   path('gallery-single', gallery_single, name = 'gallery-single'),
   path('gallery', gallery, name = 'gallery')
]
