from django.urls import path, include
from django.contrib.auth.models import User
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'moving-company', MovingCompanyViewSet, basename="moving_company")
router.register(r'moving-reservation', MovingReservationViewSet, basename="moving_reservation")
router.register(r'customer-information', CustomerInformationViewSet, basename="customer_information")
router.register(r'customer-feedbacks', CustomerFeedbackLogViewSet, basename="customer_feedback_log")

urlpatterns = [
    path('admin/', admin.site.urls),

    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]