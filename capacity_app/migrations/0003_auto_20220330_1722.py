# Generated by Django 3.2.8 on 2022-03-30 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capacity_app', '0002_alter_financeprocurementapprovaldata_request_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='projectplannerdata',
            name='request_id',
            field=models.CharField(max_length=128),
        ),
        migrations.AlterField(
            model_name='projectplannerhistorydata',
            name='request_id',
            field=models.CharField(max_length=128),
        ),
    ]
