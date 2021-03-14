from rest_framework import serializers
from django import forms
from .models import *

class WishSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wish
        exclude = ['owner']

class FulfilledSerializer(forms.ModelForm):
    class Meta:
        model = Wish
        fields = ['title' , 'acquired']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
        }
