# Generated by Django 5.1.4 on 2025-04-13 10:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EduVance', '0019_teacherreg_teacherid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='teacherreg',
            name='teacherid',
        ),
    ]
