from django.urls import path

from . import views

urlpatterns = [
  path('', views.contact_sub, name='contact_sub'),
  path('enquiry', views.contact_specific, name='contact_specific')
]