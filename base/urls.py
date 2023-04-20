from django.urls import path

from .views import *

app_name = 'base'

urlpatterns = [

    path('', l, name = 'l'),

    path('$/', payments_http),

    path('contact-us/', contact_us, name = 'contact-us'),
    path('c/', cs, name = 'cs'),

    path('terms/', terms),
    path('privacy/', privacy),
    path('juridical-information/', juridical),
    #path('data-safety/', ds, name = 'ds'),
    #path('payment-safety/', ps, name = 'ps'),
    
    #path('online-payment-safety/', ops, name = 'ops'),
    #path('data-safety/', ds, name = 'ds'),

]