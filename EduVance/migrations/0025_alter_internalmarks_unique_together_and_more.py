# Generated by Django 5.1.4 on 2025-04-19 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EduVance', '0024_delete_subjects'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='internalmarks',
            unique_together=set(),
        ),
        migrations.AlterField(
            model_name='internalmarks',
            name='subject',
            field=models.CharField(max_length=100),
        ),
        migrations.RemoveField(
            model_name='internalmarks',
            name='subjects',
        ),
    ]
