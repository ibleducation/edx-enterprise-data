# -*- coding: utf-8 -*-
"""
Views for enterprise api version 0 endpoint.
"""
from __future__ import absolute_import, unicode_literals

from logging import getLogger

from rest_framework import generics
from edx_rest_framework_extensions.paginators import DefaultPagination

from enterprise_data import models
from enterprise_data.api.v0 import serializers
from enterprise_data.api.filters import EnterpriseFilterBackend

LOGGER = getLogger(__name__)


class EnterpriseEnrollmentsView(generics.ListAPIView):
    serializer_class = serializers.EnterpriseEnrollmentSerializer
    pagination_class = DefaultPagination
    queryset = models.EnterpriseEnrollment.objects.all()

    # filter_backends = (EnterpriseFilterBackend,)
    # ENTERPRISE_ID_FILTER = 'enterprise_id'