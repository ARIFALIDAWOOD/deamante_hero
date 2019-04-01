from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.buy, name='buy'),
    path('<int:buy_id>', views.listing_buy, name='listing_buy'),
    path('search', views.search, name='search')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
