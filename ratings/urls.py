from django.urls import path
from .views import home, edit_rating, delete_rating

urlpatterns = [
    path('', home, name='ratings-home'),# This allows /beer_rater/ to load
    path('rating/edit/<int:row_id>/', edit_rating, name='rating-edit'),
    path('rating/delete/<int:row_id>/', delete_rating, name='rating-delete'),
      
]
