# Generated by Django 5.1.4 on 2025-03-07 06:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EduVance', '0017_alter_attendance_current_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Internals',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=40)),
                ('mark', models.IntegerField()),
                ('login_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EduVance.studentreg')),
                ('ta_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EduVance.teacherreg')),
            ],
        ),
    ]
