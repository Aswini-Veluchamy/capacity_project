# Generated by Django 3.2.8 on 2022-03-09 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capacity_app', '0009_financeprocurementapprovaldata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='financeprocurementapprovaldata',
            name='approved_at',
            field=models.DateTimeField(),
        ),
    ]
