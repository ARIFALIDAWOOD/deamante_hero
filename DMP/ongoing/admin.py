from django.contrib import admin

# Register your models here.
from .models import Ongoing


class OngoingAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'list_date')

    def user_info(self, obj):
        return obj.designation


admin.site.register(Ongoing, OngoingAdmin)
