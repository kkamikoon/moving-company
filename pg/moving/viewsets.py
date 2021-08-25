from rest_framework import viewsets

from .serializers import (
    MovingCompanySerializer,
    MovingReservationSerializer,
    CustomerInformationSerializer,
    CustomerFeedbackLogSerializer
)
from .models import (
    MovingCompany,
    MovingReservation,
    CustomerInformation,
    CustomerFeedbackLog,
)

class MovingCompanyViewSet(viewsets.ModelViewSet):
    queryset = MovingCompany.objects.all()
    serializer_class = MovingCompanySerializer
    http_method_names = ['get', 'post']


class MovingReservationViewSet(viewsets.ModelViewSet):
    queryset = MovingReservation.objects.all()
    serializer_class = MovingReservationSerializer
    http_method_names = ['get', 'post']


class CustomerInformationViewSet(viewsets.ModelViewSet):
    queryset = CustomerInformation.objects.all()
    serializer_class = CustomerInformationSerializer
    http_method_names = ['get', 'post']
    

class CustomerFeedbackLogViewSet(viewsets.ModelViewSet):
    queryset = CustomerFeedbackLog.objects.all()
    serializer_class = CustomerFeedbackLogSerializer
    http_method_names = ['get', 'post']
