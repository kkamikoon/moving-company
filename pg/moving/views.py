from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

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

from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.permissions import (
    IsAuthenticated
)

class MovingCompanyAPI(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        queryset = MovingCompany.objects.all()
        serializer = MovingCompanySerializer(queryset, many=True)

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