from django.shortcuts import render
from django.urls import reverse_lazy
from .forms import ContactForm
from .models import Contact
from django.views.generic import CreateView

from django.contrib import messages

from django.conf import settings
from django.core.mail import send_mail



class ContactView(CreateView):
    model=Contact
    template_name="index.html"
    form_class=ContactForm
    success_url=reverse_lazy("contact")
    def form_valid(self, form):
        
        messages.success(
            self.request, 'Your message has been sent successfully')
        
        full_name = form.cleaned_data['name']
        email = form.cleaned_data['email']
        print(email)
        message = form.cleaned_data['message']
        phone= form.cleaned_data['phone_number']
        
        text = f'Ad Soyad: {full_name} \nElektron poçt ünvanı: {email} \nMobil nömrə: {phone} \nMüraciət mətni: {message}'
        send_mail(
            'Yeni müştəri müraciəti',
            text,
            settings.EMAIL_HOST_USER,
            ['lmanmiriyeva@gmail.com'],
            fail_silently=False,
        )
        print("YES")
        self.object = form.save()

        return super().form_valid(form)
    




