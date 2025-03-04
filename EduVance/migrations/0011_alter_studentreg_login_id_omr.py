# Generated by Django 5.1.4 on 2025-03-04 06:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('EduVance', '0010_answer_t_id_essay_tea_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentreg',
            name='login_id',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='student_as_loginid', to='EduVance.login'),
        ),
        migrations.CreateModel(
            name='Omr',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('omr', models.FileField(upload_to='uploads/')),
                ('current_date', models.DateTimeField(auto_now_add=True)),
                ('login_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EduVance.login')),
                ('tc_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='EduVance.teacherreg')),
            ],
        ),
    ]
