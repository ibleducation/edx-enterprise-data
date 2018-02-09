# -*- coding: utf-8 -*-
"""
Filters for enterprise data API.
"""
from __future__ import absolute_import, unicode_literals

from rest_framework import filters

class UserFilterBackend(filters.BaseFilterBackend):
    """
    Filter backend for any view that needs to filter against the requesting user's ID.

    * Staff users will bypass this filter.
    * Non-staff users will receive only those objects that match their own user ID.

    This requires that `USER_ID_FILTER` be set in the view as a class variable, to identify
    the object's relationship to a user ID.
    """

    def filter_queryset(self, request, queryset, view):
        """
        Filter only for the user's ID if non-staff.
        """
        if not request.user.is_staff:
            filter_kwargs = {view.USER_ID_FILTER: request.user.id}
            queryset = queryset.filter(**filter_kwargs)
        return queryset