from django.db import models

# Create your models here.
class Contact(models.Model):
    fullname = models.CharField(max_length=300, default='Ali Amini')
    phone_number = models.CharField(max_length=11, unique=True)
    email_address = models.EmailField(unique=True)

    def __str__(self):
        return self.fullname
