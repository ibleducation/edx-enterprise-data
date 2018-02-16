# -*- coding: utf-8 -*-
"""
Filters for enterprise data API.
"""
from __future__ import absolute_import, unicode_literals

from rest_framework import filters

class EnterpriseFilterBackend(filters.BaseFilterBackend):
    """
    Filter backend for any view that needs to filter against the requesting user's enterprise.

    * Staff users will bypass this filter.
    * Non-staff users will receive only those objects that match the enterprise in the request

    This requires that `ENTERPRISE_ID_FILTER` be set in the view as a class variable, to identify
    the object's relationship to a enterprise ID.
    """

    def filter_queryset(self, request, queryset, view):
        """
        Filter only for the user's ID if non-staff.
        """
        enterprise_id = request.query_params.get('enterprise_id', None) if request.user.is_staff \
            else request.user.enterprise_id

        filter_kwargs = {view.ENTERPRISE_ID_FILTER: request.user.enterprise_id}
        return queryset.filter(**filter_kwargs)
