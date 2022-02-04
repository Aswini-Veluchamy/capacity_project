# Generated by Django 3.0.6 on 2022-02-04 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CapacityData',
            fields=[
                ('request_id', models.CharField(max_length=128, primary_key=True, serialize=False)),
                ('updated_time', models.CharField(max_length=128)),
                ('project_name', models.CharField(max_length=128)),
                ('data_center', models.CharField(max_length=5)),
                ('user_id', models.CharField(max_length=64)),
                ('std_stable_1', models.FloatField()),
                ('std_stable_2', models.FloatField()),
                ('std_arbor', models.FloatField()),
                ('stable_1', models.FloatField()),
                ('stable_2', models.FloatField()),
                ('arbor', models.FloatField()),
                ('gravit', models.FloatField()),
                ('move_group_name', models.CharField(max_length=64)),
                ('remarks', models.CharField(max_length=256)),
                ('tkt_status', models.CharField(max_length=16)),
            ],
        ),
    ]
