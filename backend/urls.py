from django.urls import path
from .views import HomePageView, ResumeView, ContactView


urlpatterns = [
    path('',HomePageView.as_view(),name='index'),
    path('linked-pages/resume/', ResumeView.as_view(), name='resume'),
    path('contact/', ContactView.as_view(), name='contact'), 
    ]
