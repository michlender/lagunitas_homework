from django.urls import path
from . import views

urlpatterns = [
    path('', views.ask_question, name='ask_question'),
    path('answer/', views.show_answer, name='show_answer'),
]