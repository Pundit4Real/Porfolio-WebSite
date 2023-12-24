from django.urls import path
from .views import *

app_name = 'backend'

urlpatterns = [
    path('',HomePageView.as_view(),name='index'),
]
