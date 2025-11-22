from django.shortcuts import render
from .models import Property, Inquiry
from .serializers import PropertySerializer, InquirySerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from users.permissions import IsAgent
from rest_framework import generics 
from django.shortcuts import get_object_or_404
from rest_framework.response import Response


# Create your views here.
#Views to list all and create properties
class PropertyListCreateView(generics.ListCreateAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = [IsAgent]

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsAgent()]
        return [IsAuthenticated()]
        
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

#View to retrieve, update, or delete a specific property
class PropertyDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer
    permission_classes = [IsAgent]

#Views to  create inquiries
class InquiryCreateView(generics.ListCreateAPIView):
    queryset = Inquiry.objects.all()
    serializer_class = InquirySerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

#View to list all inquiries
class InquiryListView(generics.ListAPIView):
    serializer_class = InquirySerializer
    permission_classes = [IsAgent]

#View to retrieve a specific inquiry, update or delete it
class InquiryDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Inquiry.objects.all()
    serializer_class = InquirySerializer
    permission_classes = [IsAgent]
    
