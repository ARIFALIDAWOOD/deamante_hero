from django.contrib import admin
from .models import News, ReviewsRental, ReviewsBuy, ReviewsOngoing
# Register your models here.


class NewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'Heading', 'list_date')

    def user_info(self, obj):
        return obj.Heading


class ReviewsOngoingAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'list_date')

    def user_info(self, obj):
        return obj.Heading


class ReviewsRentalAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'list_date')

    def user_info(self, obj):
        return obj.Heading


class ReviewsBuyAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'list_date')

    def user_info(self, obj):
        return obj.Heading


admin.site.register(News, NewsAdmin)
admin.site.register(ReviewsRental, ReviewsOngoingAdmin)
admin.site.register(ReviewsBuy, ReviewsBuyAdmin)
admin.site.register(ReviewsOngoing, ReviewsRentalAdmin)
