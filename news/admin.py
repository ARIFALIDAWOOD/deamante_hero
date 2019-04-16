from django.contrib import admin
from .models import News, Review
# Register your models here.


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'Heading', 'list_date')

    def user_info(self, obj):
        return obj.Heading


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'list_date')

    def user_info(self, obj):
        return obj.Heading


admin.site.register(News, NewsAdmin)
admin.site.register(Review, ReviewAdmin)
