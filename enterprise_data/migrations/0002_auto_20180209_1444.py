# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enterprise_data', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='enterpriseenrollment',
            table='enterprise_enrollment',
        ),
    ]
