from rest_framework import serializers
from .models import Contact


class ContactSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Contact
        fields = ['fullname', 'phone_number', 'email_address']