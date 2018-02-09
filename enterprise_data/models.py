# -*- coding: utf-8 -*-
"""
Database models for enterprise data.
"""
from logging import getLogger

from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _

LOGGER = getLogger(__name__)

@python_2_unicode_compatible
class EnterpriseEnrollment(models.Model):
    """
    TODO: docstring
    """
    class Meta:
        app_label = 'enterprise_data'
        db_table = 'enterprise_enrollment'
        verbose_name = _("Enterprise Enrollment")
        verbose_name_plural = _("Enterprise Enrollments")

    enterprise_id = models.CharField(max_length=255)
    enterprise_name = models.CharField(max_length=255)
    lms_user_id = models.CharField(max_length=255)
    enterprise_user_id = models.CharField(max_length=255)
    course_id = models.CharField(max_length=255, null=False, help_text='The course the learner is enrolled in.')
    enrollment_created_timestamp = models.DateTimeField()
    user_current_enrollment_mode = models.CharField(max_length=64)
    consent_granted = models.BooleanField()
    letter_grade = models.CharField(max_length=1)
    has_passed = models.BooleanField()
    passed_timestamp = models.DateTimeField()
    enterprise_sso_user_id = models.CharField(max_length=255)
    course_title = models.CharField(max_length=255)
    course_start = models.DateTimeField()
    course_end = models.DateTimeField()
    course_pacing_type = models.CharField(max_length=255)
    course_duration_weeks = models.PositiveIntegerField()
    course_min_effort = models.CharField(max_length=100)
    course_max_effort = models.CharField(max_length=100)
    user_account_creation_date = models.DateTimeField()
    user_email = models.CharField(max_length=255)
    user_username = models.CharField(max_length=255)
    user_age = models.PositiveIntegerField()
    user_level_of_education = models.CharField(max_length=6)
    user_gender = models.CharField(max_length=6)

    def __str__(self):
        """
        Return a human-readable string representation of the object.
        """
        return "<Enterprise Enrollment for {learner} in {course}>".format(
            learner=self.enterprise_user_id,
            course=self.course_id
        )

    def __repr__(self):
        """
        Return uniquely identifying string representation.
        """
        return self.__str__()