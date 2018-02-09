# -*- coding: utf-8 -*-
"""
Serializers for enterprise api version 0 endpoint.
"""

from rest_framework import serializers
from enterprise_data.models import EnterpriseEnrollment

class EnterpriseEnrollmentSerializer(serializers.ModelSerializer):
    """
    Serializer for EnterpriseEnrollment model.
    """

    class Meta:
        model = EnterpriseEnrollment
        fields = '__all__'