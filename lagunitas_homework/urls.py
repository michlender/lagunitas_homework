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
from django.urls import path, re_path, include
from django.contrib import admin

from ratings.views import home, RatingCreate, delete, edit, add_new, add

urlpatterns = [
    path('', include('homepage.urls')),  # This links the homepage app
    path('beer_rater/', include('ratings.urls')),  # Your existing app
    path('admin/', admin.site.urls),  # Admin panel
    
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^$', RatingCreate.as_view(), name='rating-home'),
    re_path(r'rating/add/$', RatingCreate.as_view(), name='rating-add'),
    re_path(r'rating/delete/(?P<row_id>[0-9]+)/$', delete , name='rating-delete'),
    re_path(r'rating/edit/(?P<row_id>[0-9]+)/$', edit , name='rating-edit'),
    re_path(r'^ajax/add/$', add_new , name='add-new'),
    re_path(r'^add/$', add , name='add'),
]
