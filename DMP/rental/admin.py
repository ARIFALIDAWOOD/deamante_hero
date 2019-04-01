from django.contrib import admin
from .models import Rental
# Register your models here.


class RentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'status')

    def user_info(self, obj):
        return obj.designation


admin.site.register(Rental, RentAdmin)
