from django.shortcuts import render
from django.http import  JsonResponse
from .models.hero import  Hero
from .models.services import ServiceHero,Services,ServicePopUp
from .models.projects import PortfolioHero, PortfolioItem, PortfolioPopup,Category
from .models.resume import ResumeHero,Education,Experience
from .models.skills import SkillsHero,Skills
from .models.testimonials import Testimonial,TestimonialHero
from .models.contact import ContactUsHero
from .forms import ContactUsForm
from .utils import EmailSender

def home(request):
    contacthero = ContactUsHero.objects.all()
    form = ContactUsForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            # Send email notification to admin
            email_sender = EmailSender()
            email_sender.send_client_email(form.instance)
            success_flag = True

            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False})  

    heroes = Hero.objects.all()
    service_heroes = ServiceHero.objects.all()
    services = Services.objects.all()
    servicepopups = [(service, ServicePopUp.objects.filter(service_title=service).first()) for service in services]
    porfolio_hero = PortfolioHero.objects.all()
    portfolio_popups = PortfolioPopup.objects.all()
    categories = Category.objects.all()
    resumeHero = ResumeHero.objects.all()
    education = Education.objects.all().order_by('-id')
    experience = Experience.objects.all().order_by('-id')
    skillshero = SkillsHero.objects.all()
    skills = Skills.objects.all().order_by('-id')
    testimonialhero = TestimonialHero.objects.all()
    testimonials = Testimonial.objects.all().order_by('-id')

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
        'resumeHero': resumeHero,
        'education': education,
        'experience': experience,
        'skillshero': skillshero,
        'skills': skills,
        'testimonialhero': testimonialhero,
        'testimonials': testimonials,
        'form': form,
        'contacthero': contacthero,
        'success_flag': success_flag if 'success_flag' in locals() else False,
    }

    return render(request, 'index.html', context)


# $('#message_sent').modal('show');
