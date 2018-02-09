# -*- coding: utf-8 -*-
"""
Views for enterprise api version 1 endpoint.
"""
from __future__ import absolute_import, unicode_literals

from logging import getLogger

from rest_framework import generics, serializers
from rest_framework.decorators import detail_route

from enterprise_data.api.v0 import models

LOGGER = getLogger(__name__)

class EnterpriseEnrollmentsView(generics.ListAPIView):
    serializer_class = serializers.ModelSerializer

    def get_queryset(self):
        """
        Retrieve the learner enrollment details for learners of the given enterprise customer

        """
        enterprise_id = self.kwargs.get('enterprise_id')
        # TODO: validate user has permission to enterprise_id

        return models.EnterpriseEnrollment.objects.filter(enterprise_id=enterprise_id)
        # TODO: pagination