from django.urls import path, re_path
from . import views
from .views import Ongoing_cbv, Ong_cbv
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.ongoing, name='ongoing'),
    path('OG_cbv/', Ongoing_cbv.as_view()),
    path('OGls_cbv/', Ong_cbv.as_view()),
    #path('<int:ongoing_id>', views.listing, name='listing'),
    re_path(r'(?P<pk>\d+)/$', Ongoing_cbv.as_view(), name='listing'),
    path('search', views.search, name='search')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
