# Generated by Django 2.2.3 on 2019-12-09 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pors_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='priapplicantjobhiredinfo',
            name='applicant_id',
            field=models.CharField(blank=True, max_length=101),
        ),
    ]
