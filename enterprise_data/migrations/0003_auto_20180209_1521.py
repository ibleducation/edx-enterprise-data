# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enterprise_data', '0002_auto_20180209_1444'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='enterpriseenrollment',
            name='country_name',
        ),
        migrations.RemoveField(
            model_name='enterpriseenrollment',
            name='user_country_code',
        ),
    ]
