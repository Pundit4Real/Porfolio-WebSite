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


class HomePageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')
class HeroView(View):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        contact_form = ContactUsForm()
        serviceModal_form = ServicePopUpForm()
        
        try:
            heroes = Hero.objects.all()
        except Exception as e:
            print(f"Error fetching heroes: {e}")
            heroes = []

        try:
            service_heroes = ServiceHero.objects.all()
        except Exception as e:
            print(f"Error fetching service heroes: {e}")
            service_heroes = []

        try:
            services = Services.objects.all()
        except Exception as e:
            print(f"Error fetching services: {e}")
            services = []
            
        try:
            contacts = ContactUsHero.objects.all()
        except Exception as e:
            print(f"Error fetching contacts: {e}")
            contacts = []

        try:
            servicepopups = [(service, ServicePopUp.objects.filter(service_title=service).first()) for service in services]
        except Exception as e:
            print(f"Error fetching service popups: {e}")
            servicepopups = []

        context = {
            'heroes': heroes,
            'service_heroes': service_heroes,
            'services': services,
            'servicepopups': servicepopups,
            'contact_form': contact_form,
            'serviceModal_form': serviceModal_form,
            'contacts': contacts
        }

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        contact_form = ContactUsForm(request.POST)
        serviceModal_form = ServicePopUpForm(request.POST)
        
        if contact_form.is_valid():
            # Process contact form submission
            client = contact_form.save()
            email = 'mohammedaalli088@gmail.com'

            if not EmailSender().send_client_email(client, email):
                messages.error(request, 'Email Alert Failed')
            return redirect('index')
        
        elif serviceModal_form.is_valid():

            client = serviceModal_form.save()
            email = 'mohammedaalli088@gmail.com'
            
            if not EmailSender().send_client_email(client, email):
                messages.error(request, 'Email Alert Failed')
            return redirect('index')
        else:
            # Display form errors in template
            for field, errors in contact_form.errors.items():
                for error in errors:
                    messages.warning(request, f"Error in {field}: {error}")
            for field, errors in serviceModal_form.errors.items():
                for error in errors:
                    messages.warning(request, f"Error in {field}: {error}")

        context = {
            'contact_form': contact_form,
            'serviceModal_form': serviceModal_form
        }
        return render(request, self.template_name, context)