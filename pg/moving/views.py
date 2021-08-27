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
        serializer = MovingCompanySerializer(queryset, many=True)

        return Response(serializer.data)

    def post(self, request):
        data = request.data
        serializer = MovingCompanySerializer(data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MovingCompanyDetailAPI(APIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get_object(self, request, pk):
        try:
            return MovingCompany.objects.get(pk=pk)
        except MovingCompany.DoesNotExist:
            raise Http404

    def get(self, request, idx, format=None):
        moving_company = self.get_object(pk)
        serializer = MovingCompanySerializer(moving_company)
        return Response(serializer.data)

    def put(self, requeest, pk, format=None):
        moving_company = self.get_object(pk)
        serializer = MovingCompanySerializer(moving_company, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MovingReservationAPI(APIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get(self, request):
        queryset = MovingReservation.object.all()
        serializer = MovingReservationSerializer(queryset, many=True)

        return Response(serializer.data)

class CustomerInformationAPI(APIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get(self, request):
        queryset = CustomerInformation.object.all()
        serializer = CustomerInformationSerializer(queryset, many=True)

        return Response(serializer.data)

class CustomerFeedbackLogAPI(APIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get(self, request):
        queryset = CustomerFeedbackLog.object.all()
        serializer = CustomerFeedbackLogSerializer(queryset, many=True)

        return Response(serializer.data)




'''
# Create your views here.
@csrf_exempt
def moving_company(request):
    # List of moving companies
    if request.method == 'GET':
        query_set = MovingCompany.objects.all()
        serializer = MovingCompanySerializer(query_set, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MovingCompanySerializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def moving_company_detail(request, idx):
    # Detail of single moving company
    obj = MovingCompany.objects.get(pk=idx)

    if request.method == 'GET':
        serializer = MovingCompanySerializer(obj)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = MovingCompanySerializer(obj, data=data)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == "DELETE":
        obj.delete()
        return HttpResponse(status=204)
'''