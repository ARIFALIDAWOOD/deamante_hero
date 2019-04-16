from django.contrib import admin
from .models import Contact,Contact_Specific


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'email', 'contact_date')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'email', 'phone')
    list_per_page = 25


admin.site.register(Contact, ContactAdmin)

class ContactSpecificAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'prop', 'prop_Id', 'phone')

admin.site.register(Contact_Specific, ContactSpecificAdmin)
