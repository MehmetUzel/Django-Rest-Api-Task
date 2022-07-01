from django.urls import path
from .views import CurrencyViews,IpViews

app_name = 'rest_api'
urlpatterns = [
    path('currency/', CurrencyViews.as_view(),name='currecy-rate'),
    path('ip/', IpViews.as_view(),name='ip-address')
]