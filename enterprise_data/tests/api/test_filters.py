# -*- coding: utf-8 -*-
"""
Tests for the `enterprise-data` filters module.
"""

from __future__ import absolute_import, unicode_literals

import ddt
import unittest
from pytest import mark
from rest_framework import status
from rest_framework.reverse import reverse

from django.conf import settings


@ddt.ddt
@mark.django_db
class TestEnterpriseFilterBackend(unittest.TestCase):
    """
    Test suite for the ``EnterpriseFilterBackend`` filter.
    """

    fixtures = ['enterprise_enrollment.json']

    # def setUp(self):
    #     self.enrollments = factories.EnterpriseCustomerFactory()

    @ddt.data(
        (False, 1),
        (True, 3),
    )
    @ddt.unpack
    def test_filter_for_staff(self, is_staff, expected_data_length):
        """
        Filter objects based off of user ID -- show all for staff, but only the authenticated user himself otherwise.

        Note that the choice of endpoint below is arbitrary.
        This test could use any endpoint that makes use of the ``UserFilterBackend`` filter.
        """
        self.user.is_staff = is_staff
        self.user.save()
        factories.EnterpriseCustomerFactory()
        response = self.client.get(settings.TEST_SERVER + reverse('enterprise-customer-list'))
        assert response.status_code == status.HTTP_200_OK
        data = self.load_json(response.content)
        assert len(data['results']) == expected_data_length
