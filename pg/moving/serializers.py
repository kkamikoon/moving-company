from rest_framework import serializers

from .models import (
    MovingCompany,
    MovingReservation,
    CustomerInformation,
    CustomerFeedbackLog,
)

class MovingCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = MovingCompany # Model 설정
        fields = (
            # 'id',
            'name',
            # 'ceo',
            'tel',
            'address',
            # 'business_number',
            # 'business_reg_date',
            # 'number_of_employees',
            # 'number_of_vehicles',
            'reservation_status'
        )

class MovingReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovingReservation
        fields = (
            # 'id',
            'name',
            'tel',
            'start_address',
            # 'start_floor',
            'end_address',
            # 'end_floor',
            'moving_date',
            'is_storage',
            # 'agreement_information_collection',
            # 'agreement_sharing_collected_information',
            # 'agreement_marketing',
        )

class CustomerInformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerInformation
        fields = (
            # 'id',
            'name',
            'tel',
            # 'reg_date',
            # 'agreement_information_collection',
            # 'agreement_sharing_collected_information',
            # 'agreement_marketing',
        )

class CustomerFeedbackLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerFeedbackLog
        fields = (
            # 'id',
            'customer',
            'company',
            'move_type',
            'agreement_open_information',
            'satisfied_pro',
            'satisfied_price',
            'satisfied_kindness',
            'revisit',
            'payment',
            'moving_date',
            'feedback_date',
            'feedback_text',
        )

