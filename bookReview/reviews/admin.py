from django.contrib import admin

# Register your models here.
from .models import Book, Review

class ReviewAdmin(admin.ModelAdmin):
    model = Review
    list_display = ('Book', 'rating', 'user_name', 'comment', 'pub_date')
    list_filter = ['pub_date', 'user_name']
    search_fields = ['comment']
    
admin.site.register(Book)
admin.site.register(Review, ReviewAdmin)