from django.shortcuts import get_object_or_404, render, redirect
from django.views import View
from django.core.mail import send_mail
from django.contrib import messages
from django.http import HttpResponseRedirect, JsonResponse
from .models.hero import  Hero
from .models.services import ServiceHero,Services,ServicePopUp
from .models.projects import PortfolioHero, PortfolioItem, PortfolioPopup,Category
from .forms import ContactUsForm,ServicePopUpForm
from .utils import EmailSender

def home(request):
    heroes = Hero.objects.all()
    service_heroes = ServiceHero.objects.all()
    services = Services.objects.all()
    servicepopups = [(service, ServicePopUp.objects.filter(service_title=service).first()) for service in services]
    porfolio_hero = PortfolioHero.objects.all()
    portfolio_popups = PortfolioPopup.objects.all()
    categories = Category.objects.all()

    selected_category = request.GET.get('category')

    if selected_category:
        if selected_category == 'All':
            portfolio_items = PortfolioItem.objects.all()
        else:
            portfolio_items = PortfolioItem.objects.filter(category__name=selected_category)
    else:
        portfolio_items = PortfolioItem.objects.all()

    context = {
        'heroes': heroes,
        'service_heroes': service_heroes,
        'services': services,
        'servicepopups': servicepopups,
        'portfolio_items': portfolio_items,
        'porfolio_hero': porfolio_hero,
        'portfolio_popups': portfolio_popups,
        'categories': categories,
        'selected_category': selected_category,
    }

    return render(request, 'index.html', context)
