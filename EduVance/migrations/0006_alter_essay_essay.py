# Generated by Django 5.1.4 on 2025-02-22 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EduVance', '0005_essay'),
    ]

    operations = [
        migrations.AlterField(
            model_name='essay',
            name='essay',
            field=models.FileField(upload_to='uploads/'),
        ),
    ]
