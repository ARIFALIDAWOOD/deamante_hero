from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.rental, name='rental'),
    path('<int:rental_id>', views.listing_rent, name='listing_rent'),
    path('search', views.search, name='search')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
