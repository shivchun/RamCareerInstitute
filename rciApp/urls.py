from django.urls import path
from rciApp import views

urlpatterns = [
    path('contact/', views.contact),
    path('engineering/', views.engineering),
    path('medical/', views.medical),
    path('foundation/', views.foundation),
    path('foundation_ex/', views.foundation_extended),
    path('thank/', views.thanku),
    path('new_batch/', views.new_batch),
    path('about/', views.about),
    path('notification/', views.notification),
]
