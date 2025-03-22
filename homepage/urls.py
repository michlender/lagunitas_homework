from django.urls import path
from .views import home, test_base

urlpatterns = [
    path('', home, name='home'),
    path('test-base/', test_base),
]
