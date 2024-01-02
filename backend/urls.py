from django.urls import path
from .views import *


urlpatterns = [
    path('',HomePageView.as_view(),name='index'),
    path('linked-pages/resume/', ResumeView.as_view(), name='resume'),
    
    ]
