from django.shortcuts import render, redirect
from django.views import View
from django.core.mail import send_mail
from django.contrib import messages
from .forms import ContactMeForm
from .models.hero import  Hero
from .models.services import ServiceHero,Services,ServicePopUp

class HomePageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html')

class ContactView(View):
    def get(self, request, *args, **kwargs):
        form = ContactMeForm()
        return render(request, 'index.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = ContactMeForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            recipient_email = 'mohammedaalli088@gmail.com'

            if email:
                full_message = f"Message from: {name}\nEmail: {email}\n\n{message}"
                try:
                    send_mail(
                        subject, 
                        full_message,
                        email, 
                        [recipient_email], 
                        fail_silently=False,
                    )
                    messages.success(request, 'Your message has been sent successfully!')
                    return redirect('#contact')  # Redirect to a thank you page or homepage
                except Exception as e:
                    messages.error(request, f"Failed to send message. Error: {e}")
            else:
                messages.warning(request, "Email address is required.")
        else:
            # Display form errors in template
            for field, errors in form.errors.items():
                for error in errors:
                    messages.warning(request, f"Error in {field}: {error}")

        return render(request, 'index.html', {'form': form})

class HeroView(View):
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        try:
            # Query all Hero objects from the database
            heroes = Hero.objects.all()
        except Exception as e:
            # Handle any exceptions
            print(f"Error fetching heroes: {e}")
            heroes = []

        try:
            # Fetch service heroes from the database
            service_heroes = ServiceHero.objects.all()
        except Exception as e:
            # Handle any exceptions
            print(f"Error fetching service heroes: {e}")
            service_heroes = []

        try:
            services = Services.objects.all()
        except Exception as e:
            print(f"Error fetching services: {e}")
            services = []

        try:
            servicepopup = ServicePopUp.objects.all()
        except Exception as e:
            print(f"Error fetching services: {e}")
            servicepopup = []

        context = {
            'heroes': heroes,
            'service_heroes': service_heroes,
            'services':services,
            'servicepopup':servicepopup
        }

        return render(request, self.template_name, context)