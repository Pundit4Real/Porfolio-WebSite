from django.shortcuts import render, redirect
from django.views import View
from django.core.mail import send_mail
from django.contrib import messages
from .forms import ContactMeForm

class HomePageView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'main/index.html')

class ResumeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'linked-pages/resume.html')

def contact(request):
    if request.method == 'POST':
        form = ContactMeForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            full_message = f"Message from: {name}\nEmail: {email}\n\n{message}"
            
            send_mail(subject, full_message, email, ['your_email@example.com'])

            messages.success(request, 'Your message has been sent Successfully!')
            return redirect('index')  
    else:
        form = ContactMeForm()
    
    return render(request, 'main/index.html', {'form': form})
