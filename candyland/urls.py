from django.urls import path
from . import views

urlpatterns = [
	path('', views.board, name='board'),
	path('move/', views.move, name='move'),
	path('win/', views.win, name='win'),
]