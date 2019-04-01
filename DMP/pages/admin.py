from django.contrib import admin
from .models import Employee, Carousel
# Register your models here.


class PagesAdmin(admin.ModelAdmin):
    list_display = ('First_name', 'designation')

    def user_info(self, obj):
        return obj.designation


class CaroAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

    def user_info(self, obj):
        return obj.name


admin.site.register(Carousel, CaroAdmin)
admin.site.register(Employee, PagesAdmin)
