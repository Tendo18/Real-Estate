from django.urls import path
from .views import PropertyListCreateView, PropertyDetailView, InquiryCreateView, InquiryListView, InquiryDetailView

urlpatterns = [
    path('properties/', PropertyListCreateView.as_view(), name='property-list-create'),
    path('properties/<int:pk>', PropertyDetailView.as_view(), name='property-detail'),
    path('inquiry/', InquiryCreateView.as_view(), name='inquiry-create'),
    path('inquiry/list/', InquiryListView.as_view(), name='inquiry-list'),
    path('inquiry/<int:pk>', InquiryDetailView.as_view(), name='inquiry-detail'),
]