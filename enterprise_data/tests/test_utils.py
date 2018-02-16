# -*- coding: utf-8 -*-
"""
Test factories.
"""

import factory
from faker import Factory as FakerFactory
from django.utils.dateparse import parse_datetime

from enterprise_data.models import EnterpriseEnrollment

FAKER = FakerFactory.create()

class EnterpriseEnrollmentFactory(factory.django.DjangoModelFactory):
    """
    EnterpriseCourseEnrollment factory.

    Creates an instance of EnterpriseCourseEnrollment with minimal boilerplate.
    """

    class Meta(object):
        """
        Meta for EnterpriseCourseEnrollmentFactory.
        """

        model = EnterpriseEnrollment

    id = factory.lazy_attribute(lambda x: FAKER.random_int(min=1))
    enterprise_id = factory.lazy_attribute(lambda x: 'Test Company')
    lms_user_id = factory.lazy_attribute(lambda x: FAKER.random_int(min=1))
    enterprise_user_id = factory.lazy_attribute(lambda  x: FAKER.random_int(min=1))
    course_id = factory.lazy_attribute(lambda x: FAKER.slug())
    enrollment_created_timestamp = factory.lazy_attribute(lambda x: '2018-01-01')
    user_current_enrollment_mode = factory.lazy_attribute(lambda x: 'verified')
