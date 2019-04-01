from django.contrib import admin
from .models import Buy
# Register your models here.


class BuyAdmin(admin.ModelAdmin):
    list_display = ('name', 'status')

    def user_info(self, obj):
        return obj.designation


admin.site.register(Buy, BuyAdmin)
