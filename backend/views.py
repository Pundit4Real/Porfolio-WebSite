from django.shortcuts import render, redirect
from django.views import View
from django.core.mail import send_mail
from django.contrib import messages
from django.http import HttpResponseRedirect, JsonResponse
from .models.hero import  Hero
from .models.services import ServiceHero,Services,ServicePopUp
from .models.contact import ContactUs,ContactUsHero
from .forms import ContactUsForm,ServicePopUpForm
from .utils import EmailSender



def home(request):
    form = ServicePopUpForm(request.POST)

    if request.method == 'POST':
        form = ServicePopUpForm(request.POST)

        if form.is_valid():
            client = form.save()

            if not EmailSender().send_client_email(client):
                messages.error(request, 'Request Fail')
            messages.success(request, 'Your Request has Been Received, We will get in contact with you ')

    heroes = Hero.objects.all()
    service_heroes = ServiceHero.objects.all()
    services = Services.objects.all()
    servicepopups = [(service, ServicePopUp.objects.filter(service_title=service).first()) for service in services]
    contacts = ContactUsHero.objects.all()
    

    print(services, 'printing servicess ')

    context = {
        'heroes': heroes,
        'service_heroes': service_heroes,
        'services': services,
        'servicepopups': servicepopups,
        'form': form,
        'contacts': contacts
    }
    return render(request, 'index.html', context)


def contact_view(request):
    form = ContactUsForm(request.POST)

    heroes = Hero.objects.all()
    service_heroes = ServiceHero.objects.all()
    services = Services.objects.all()
    servicepopups = [(service, ServicePopUp.objects.filter(service_title=service).first()) for service in services]
    contacts = ContactUs.objects.all()

    context = {
        'heroes': heroes,
        'service_heroes': service_heroes,
        'services': services,
        'servicepopups': servicepopups,
        'form': form,
        'contacts': contacts
    }
    return render(request, 'index.html',context)