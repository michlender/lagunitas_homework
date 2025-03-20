from django.contrib import admin
from .models import Rating  # Import your model if it exists

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('id', 'beer_name', 'score')  # Adjust fields as needed

