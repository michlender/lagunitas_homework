from django.urls import path
from .views import RatingCreate, delete, edit, add_new, add

urlpatterns = [
    path('', RatingCreate.as_view(), name='rating-home'),  # Default view when visiting /beer_rater/
    path('add/', RatingCreate.as_view(), name='rating-add'),
    path('rating/edit/<int:row_id>/', edit, name='rating-edit'),
    path('rating/delete/<int:row_id>/', delete, name='rating-delete'),
    path('edit/<int:row_id>/', edit, name='rating-edit'),
]

#from django.urls import path
#from .views import home, edit_rating, delete_rating, add_rating
#
#urlpatterns = [
#    path('ratings/', home, name='rating-home'),# This allows /beer_rater/ to load
#    path('add/', add_rating, name='rating-add'),
#    path('rating/edit/<int:row_id>/', edit_rating, name='rating-edit'),
#    path('rating/delete/<int:row_id>/', delete_rating, name='rating-delete'),
#    path('edit/<int:row_id>/', edit_rating, name='rating-edit'),
#      
#]
