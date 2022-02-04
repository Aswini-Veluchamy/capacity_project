from django.db import models


class CapacityData(models.Model):
    request_id = models.CharField(max_length=128, primary_key=True)
    updated_time = models.CharField(max_length=128)
    project_name = models.CharField(max_length=128)
    data_center = models.CharField(max_length=5)
    user_id = models.CharField(max_length=64)
    std_stable_1 = models.FloatField()
    std_stable_2 = models.FloatField()
    std_arbor = models.FloatField()
    stable_1 = models.FloatField()
    stable_2 = models.FloatField()
    arbor = models.FloatField()
    gravit = models.FloatField()
    move_group_name = models.CharField(max_length=64)
    remarks = models.CharField(max_length=256)
    tkt_status = models.CharField(max_length=16)

