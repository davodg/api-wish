from django.shortcuts import render
from django.views.generic import UpdateView
from django.urls import reverse
from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import *
from .serializers import *


class RandomView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def random(self, request, format=None):
        obj = Wish.objects.order_by('?')[0]
        context = {
            'object': obj
        }
        content = {
        'id_wish': obj.id_wish, 
        'title': obj.title, 
        'description': obj.description,
        'link': obj.link,
        'image': obj.image,
        'acquired': obj.acquired,
        }
        return Response(content)

    def get(self, request):
        return self.random(request)
    

class WishViewSet(viewsets.ModelViewSet):
    serializer_class = WishSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):
        return Wish.objects.filter(owner=self.request.user)

class FulfilledView(UpdateView):
    model = Wish
    form_class = FulfilledSerializer
    permission_classes = (permissions.IsAuthenticated,)
    template_name = 'update_wish.html'

    def get_success_url(self):
        return reverse('update_post')



