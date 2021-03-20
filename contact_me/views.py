from django.shortcuts import render

# Create your views here.
from django.views.generic import CreateView

from .forms import ContactMeForm


class ContactMe(CreateView):
    template_name = 'contact.html'
    form_class = ContactMeForm

    def form_valid(self, form):
        # name = form.cleaned_data.get('name')
        # surname = form.cleaned_data.get('surname')
        # email = form.cleaned_data.get('email')
        # customers_message = form.cleaned_data.get('message')
        # message = f'Message from {name} {surname}\n'
        # message += f'\n\n{customers_message}'
        # message += f'Contacts:\nE-mail: {email}'
        # send_mail(
        #     subject=f'New booked lesson from {name} {surname}!',
        #     message=message,
        #     from_email='contact-form@myapp.com',
        #     recipient_list=[email, '@owners_email'],
        # )

        return super().form_valid(form)
