# Generated by Django 3.2.8 on 2022-03-09 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capacity_app', '0007_milestonedata'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProjectPlannerHistoryData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_center', models.CharField(max_length=128)),
                ('project_name', models.CharField(max_length=128)),
                ('user_name', models.CharField(max_length=128)),
                ('milestone_name', models.CharField(max_length=128)),
                ('date', models.CharField(max_length=128)),
                ('std_stable1', models.IntegerField()),
                ('std_stable2', models.IntegerField()),
                ('std_arbor', models.IntegerField()),
                ('stable1', models.IntegerField()),
                ('stable2', models.IntegerField()),
                ('arbor', models.IntegerField()),
                ('gravit', models.IntegerField()),
                ('remarks', models.CharField(max_length=200)),
                ('financial_approval', models.BooleanField()),
                ('procurement_approval', models.BooleanField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'project_planner_history_data',
            },
        ),
    ]
