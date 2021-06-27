from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from interview.views import InterViewSlots, RegisterSlot


# router = routers.DefaultRouter()
# router.register(r'register-slot', RegisterSlot)


urlpatterns = [
    path('register-slot/', RegisterSlot.as_view()),
    path('slots/<int:candidate>/<int:interviewer>/', InterViewSlots.as_view()),
]
