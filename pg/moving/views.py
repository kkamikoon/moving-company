# Django
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import Http404

# REST Framework
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework import status

from .models import (
    MovingCompany,
    MovingReservation,
    CustomerInformation,
    CustomerFeedbackLog,
)
from .serializers import (
    MovingCompanySerializer,
    MovingReservationSerializer,
    CustomerInformationSerializer,
    CustomerFeedbackLogSerializer
)

class MovingCompanyAPI(APIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get(self, request):
        queryset = MovingCompany.objects.all()

        for q in queryset:
            q.tel = self.tel_masking(q.tel) # Tel Masking
            q.address = self.address_filtering(q.address) # Address filtering

        serializer = MovingCompanySerializer(queryset, many=True)

        res = { "total_data_count"  : len(queryset),
                "result"            : serializer.data }

        return Response(res)

    def tel_masking(self, tel):
        s_tel = tel.split("-")
        s_tel[-1] = s_tel[-1][0] + '*'*2 + s_tel[-1][-1]

        return "-".join(s_tel)

    def address_filtering(self, addr):
        s_addr = addr.split(" ")

        return " ".join(s_addr[:3])
        

class MovingCompanyDetailAPI(APIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_object(self, pk):
        try:
            return MovingCompany.objects.get(pk=pk)
        except MovingCompany.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        moving_company = self.get_object(pk)
        moving_company.tel = self.tel_masking(moving_company.tel) # Tel masking
        moving_company.address = self.address_filtering(moving_company.address) # Address Filtering

        serializer = MovingCompanySerializer(moving_company)

        return Response(serializer.data)
        
    def tel_masking(self, tel):
        s_tel = tel.split("-")
        s_tel[-1] = s_tel[-1][0] + '*'*2 + s_tel[-1][-1]

        return "-".join(s_tel)

    def address_filtering(self, addr):
        s_addr = addr.split(" ")

        return " ".join(s_addr[:3])


class MovingReservationAPI(APIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get(self, request):
        queryset = MovingReservation.objects.all()

        for q in queryset:
            q.tel = self.tel_masking(q.tel) # Tel Masking
            q.start_address = self.address_filtering(q.start_address) # Start Address filtering
            q.end_address   = self.address_filtering(q.end_address)   # End Address filtering
            q.moving_date   = self.date_format(q.moving_date)         # Moving date formatting

        serializer = MovingReservationSerializer(queryset, many=True)

        res = { "total_data_count"  : len(queryset),
                "result"            : serializer.data }

        return Response(res)

    def tel_masking(self, tel):
        s_tel = tel.split("-")
        s_tel[-1] = s_tel[-1][0] + '*'*2 + s_tel[-1][-1]

        return "-".join(s_tel)

    def address_filtering(self, addr):
        s_addr = addr.split(" ")

        return " ".join(s_addr[:3])
    
    def date_format(self, date):
        return date.strftime("%Y-%m-%d")


class MovingReservationDetailAPI(APIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_object(self, pk):
        try:
            return MovingReservation.objects.get(pk=pk)
        except MovingReservation.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        moving_reservation = self.get_object(pk)
        moving_reservation.tel = self.tel_masking(moving_reservation.tel) # Tel masking
        moving_reservation.start_address = self.address_filtering(moving_reservation.start_address) # Start Address
        moving_reservation.end_address = self.address_filtering(moving_reservation.end_address) # End Address 
        moving_reservation.moving_date = self.date_format(moving_reservation.moving_date) # Moving Date
        serializer = MovingReservationSerializer(moving_reservation)

        return Response(serializer.data)
        
    def tel_masking(self, tel):
        s_tel = tel.split("-")
        s_tel[-1] = s_tel[-1][0] + '*'*2 + s_tel[-1][-1]

        return "-".join(s_tel)

    def address_filtering(self, addr):
        s_addr = addr.split(" ")

        return " ".join(s_addr[:3])

    def date_format(self, date):
        return date.strftime("%Y-%m-%d")



class CustomerInformationAPI(APIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get(self, request):
        queryset = CustomerInformation.objects.all()

        for q in queryset:
            q.tel = self.tel_masking(q.tel) # Tel Masking

        serializer = CustomerInformationSerializer(queryset, many=True)

        res = { "total_data_count"  : len(queryset),
                "result"            : serializer.data }

        return Response(res)

    def tel_masking(self, tel):
        s_tel = tel.split("-")
        s_tel[-1] = s_tel[-1][0] + '*'*2 + s_tel[-1][-1]

        return "-".join(s_tel)


class CustomerInformationDetailAPI(APIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_object(self, pk):
        try:
            return CustomerInformation.objects.get(pk=pk)
        except CustomerInformation.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        customer_info = self.get_object(pk)
        serializer = CustomerInformationSerializer(customer_info)

        customer_info.tel = self.tel_masking(customer_info.tel)

        return Response(serializer.data)
        
    def tel_masking(self, tel):
        s_tel = tel.split("-")
        s_tel[-1] = s_tel[-1][0] + '*'*2 + s_tel[-1][-1]

        return "-".join(s_tel)


class CustomerFeedbackLogAPI(APIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get(self, request):
        queryset = CustomerFeedbackLog.objects.all()
        serializer = CustomerFeedbackLogSerializer(queryset, many=True)

        for q in queryset:
            q.moving_date = self.date_format(q.moving_date)
            q.feedback_date = self.date_format(q.feedback_date)

        res = { "total_data_count"  : len(queryset),
                "result"            : serializer.data }

        return Response(res)
    
    def date_format(self, date):
        return date.strftime("%Y-%m-%d")


class CustomerFeedbackLogDetailAPI(APIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_object(self, pk):
        try:
            return CustomerFeedbackLog.objects.get(pk=pk)
        except CustomerFeedbackLog.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        customer_info = self.get_object(pk)

        serializer = CustomerFeedbackLogSerializer(customer_info)

        customer_info.moving_date = self.date_format(customer_info.moving_date)
        customer_info.feedback_date = self.date_format(customer_info.feedback_date)

        return Response(serializer.data)
        
    def date_format(self, date):
        return date.strftime("%Y-%m-%d")


