from django.urls import path
from .views import HomePageView, HeroView


urlpatterns = [
    path('', HeroView.as_view(), name='index'),
    # path('contact/', ContactView.as_view(), name='contact'),
]
