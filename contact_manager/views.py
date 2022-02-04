from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from contact_manager.models import Contact
from .serializers import ContactSerializer
from rest_framework import viewsets

# Create your views here.
class CreateContact(CreateView):
    model= Contact
    fields = ['fullname', 'phone_number', 'email_address']


class ContactLists(ListView):
    model = Contact
    queryset = Contact.objects.all()



class ContactDelete(DeleteView):
    model= Contact
    success_url = reverse_lazy('contact_manager:contact_lists')


class ContactUpdate(UpdateView):
    model = Contact
    fields = ['fullname', 'phone_number', 'email_address']
    template_name = 'contact_manager/contact_update.html'


class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer