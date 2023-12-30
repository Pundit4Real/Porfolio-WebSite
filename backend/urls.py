from django.urls import path
from .views import *


urlpatterns = [
    path('',HomePageView.as_view(),name='index'),
    path('details/',DetailsPageView.as_view(),name='portfolio-details-page'),
]
