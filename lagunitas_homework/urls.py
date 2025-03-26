"""beer_rater URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.urls import path, include, re_path
from django.contrib import admin
from ratings.views import RatingCreate, delete, edit, add_new, add

urlpatterns = [
    path('admin/', admin.site.urls),  # Keep only one admin path
    path('', include('homepage.urls')),  # Set homepage as root
    path('ratings/', include('ratings.urls')),  # App link
    
    # Ratings-related paths
    path('ratings/add/', RatingCreate.as_view(), name='rating-add'),
    path('ratings/delete/<int:row_id>/', delete, name='rating-delete'),
    path('ratings/edit/<int:row_id>/', edit, name='rating-edit'),
    path('ajax/add/', add_new, name='add-new'),
    path('add/', add, name='add'),
]
