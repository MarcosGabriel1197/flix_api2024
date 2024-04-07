from django.contrib import admin
from review.models import Review


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('id', 'movie', 'stars', 'comment')
