from django.db import models
from django.urls import reverse

# Create your models here.
class Contact(models.Model):
    fullname = models.CharField(max_length=300, default='Ali Amini')
    phone_number = models.CharField(max_length=11, unique=True)
    email_address = models.EmailField(unique=True)

    def __str__(self):
        return self.fullname


    def get_absolute_url(self):
        return reverse('contact_manager:contact_lists')
     
