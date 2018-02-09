# -*- coding: utf-8 -*-
"""
Views for enterprise api version 0 endpoint.
"""
from __future__ import absolute_import, unicode_literals

from logging import getLogger

from rest_framework import generics

from enterprise_data import models
from enterprise_data.api.v0 import serializers

LOGGER = getLogger(__name__)

class EnterpriseEnrollmentsView(generics.ListAPIView):
    serializer_class = serializers.EnterpriseEnrollmentSerializer

    def get_queryset(self):
        """
        Retrieve the learner enrollment details for learners of the given enterprise customer

        """
        enterprise_id = self.kwargs.get('enterprise_id')
        # TODO: validate user has permission to enterprise_id

        return models.EnterpriseEnrollment.objects.filter(enterprise_id=enterprise_id)
        # TODO: pagination