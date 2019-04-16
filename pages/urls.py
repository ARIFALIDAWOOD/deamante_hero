from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.index, name='index'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('Coming-Soon', views.coming, name='coming')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# print(settings.STATIC_URL)
