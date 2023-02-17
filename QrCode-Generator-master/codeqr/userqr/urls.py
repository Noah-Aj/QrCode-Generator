from django.urls import path
from .views import home

app_name = 'user-code'

urlpatterns = [
    path('', home, name='home'),
]
