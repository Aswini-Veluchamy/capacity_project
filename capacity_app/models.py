from django.db import models

class CapacityData(models.Model):
    request_id = models.CharField(max_length=128, primary_key=True)
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField()
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

    def __str__(self):
        return self.request_id

    class Meta:
        db_table = "request_capacity_data"


class HistoryData(models.Model):
    project_name = models.CharField(max_length=128)
    request_id = models.CharField(max_length=128)
    updated_time = models.DateTimeField()
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

    def __str__(self):
        return self.project_name

    class Meta:
        db_table = "history_capacity_data"
