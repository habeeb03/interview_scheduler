from .models import Person
from rest_framework import (
    routers, 
    serializers, 
    views, 
    status
)
from rest_framework.response import Response
from rest_framework import viewsets, views, serializers
from . import models
from .serializers import PersonSerializer
from datetime import timedelta, datetime


class RegisterSlot(views.APIView):

    def post(self, request):
        serializer = PersonSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
            
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class InterViewSlots(views.APIView):

    def get(self, request, candidate, interviewer):
        interviewer = models.Person.objects.get(pk=interviewer)
        candidate = models.Person.objects.get(pk=candidate)

        interviewer_slots = interviewer.timeslot_set.values_list('from_time', 'to_time')
        candidate_slots = candidate.timeslot_set.values_list('from_time', 'to_time')

        possible_slots = []

        interviewer_from_slot = interviewer_slots[0][0]
        interviewer_to_slot = interviewer_slots[0][1]

        candidate_from_slot = candidate_slots[0][0]
        candidate_to_slot = candidate_slots[0][1]


        from_time = interviewer_from_slot
        while(from_time < interviewer_to_slot):
            time = datetime.combine(datetime.now().date(), from_time) + timedelta(hours=1)
            time = time.time()

            if time >= candidate_from_slot and time <= candidate_to_slot:
                possible_slots.append({'from': str(from_time), 'to': str(time)})

            from_time = time

        return Response({
            'slots': tuple(possible_slots)
        })


