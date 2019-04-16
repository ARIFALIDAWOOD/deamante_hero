from django.urls import path, re_path
from . import views
from .views import Ongoing_cbv, Ong_cbv, Buyls_cbv, Rentls_cbv, Allls_cbv, Searchls_cbv
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('upcoming/', Ong_cbv.as_view(), name='ongoing'),
    path('buy/', Buyls_cbv.as_view(), name='buy'),
    path('rent/', Rentls_cbv.as_view(), name='rental'),
    path('all/', Allls_cbv.as_view(), name='all'),
    re_path(r'(?P<pk>\d+)/$', Ongoing_cbv.as_view(), name='listing'),
    path('search', Searchls_cbv.as_view(), name='search')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
