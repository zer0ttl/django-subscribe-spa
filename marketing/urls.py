from django.contrib import admin
from django.urls import path, include

from .views import email_list_signup, home_page


urlpatterns = [
    path('', home_page, name='home'),
    path('subscribe/', email_list_signup, name='subscribe'),
]
