from django.contrib import admin

# Register your models here.
from .models import Listing


class ListingsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'list_date')

    def user_info(self, obj):
        return obj.designation


admin.site.register(Listing, ListingsAdmin)
