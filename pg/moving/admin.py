from django.contrib import admin
from .models import (
    MovingCompany,
    MovingReservation,
    CustomerInformation,
    CustomerFeedbackLog,
)

# Register your models here.
admin.site.register(MovingCompany)
admin.site.register(MovingReservation)
admin.site.register(CustomerInformation)
admin.site.register(CustomerFeedbackLog)
