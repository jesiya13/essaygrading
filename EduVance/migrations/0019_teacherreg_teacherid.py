# Generated by Django 5.1.4 on 2025-04-13 10:30

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EduVance', '0018_studentsubjectselection'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacherreg',
            name='teacherid',
            field=models.CharField(default=uuid.uuid4, editable=False, max_length=40, unique=True),
        ),
    ]
