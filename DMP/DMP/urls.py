from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static

from ongoing.views import Ongoing_cbv

urlpatterns = [
    path('', include('pages.urls')),
    path('listings/', include('ongoing.urls')),
    #re_path(r'^listings/(?P<pk>\d+)/$', Ongoing_cbv.as_view(), name='listing'),
    path('buy/', include('buy.urls')),
    path('rentals/', include('rental.urls')),
    path('accounts/', include('accounts.urls')),
    path('contacts/', include('contacts.urls')),
    path('admin/', admin.site.urls),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
