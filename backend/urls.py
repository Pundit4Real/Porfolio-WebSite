from django.urls import path
from .views import HomePageView, ContactView, HeroView

urlpatterns = [
    path('', HeroView.as_view(), name='index'),
    path('contact/', ContactView.as_view(), name='contact'),
    # path('heroes/', HeroView.as_view(), name='hero-list'),  # Add this line for HeroView
]
