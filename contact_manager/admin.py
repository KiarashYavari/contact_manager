from django.contrib import admin
from .models import Contact
# Register your models here.
class AdminContact(admin.ModelAdmin):
    list_display = ['fullname', 'phone_number', 'email_address']

admin.site.register(Contact, AdminContact)