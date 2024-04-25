from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    # path('', contact_us, name='home'),
    path('<int:pk>/', home, name='portfolio_detail'),

]
