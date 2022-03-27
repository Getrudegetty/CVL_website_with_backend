from email import message
from multiprocessing import context
from pyexpat import model
from django.shortcuts import render
from django.contrib import messages
from .models import About, Services, Services_More
from django.views import generic
from . forms import ContactForm

# Create your views here.

class IndexView(generic.TemplateView):
    template_name = 'cvl_app/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        services = Services.objects.filter(is_active=True)
        services_more = Services_More.objects.filter(is_active=True)
        about = About.objects.filter(is_active=True)

        context['services'] = services
        context['services_more'] = services_more
        context['about'] = about
        return context

class ServicesView(generic.ListView):
    model = Services
    template_name = 'cvl_app/Services.html'
    paginate_by = 10

    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)

class ContactView(generic.FormView):
    template_name = 'cvl_app/contact.html'
    form_class = ContactForm
    success_url = "/"

    def form_valid(self, form):
        form.save()
        messages.success(self.request, 'Thank you for reaching out. We will be in touch soon')
        return super().form_valid(form)

