from django.db import models


class ProjectPlannerData(models.Model):
    data_center = models.CharField(max_length=128)
    project_name = models.CharField(max_length=128)
    user_name = models.CharField(max_length=128)
    milestone_name = models.CharField(max_length=128)
    date = models.CharField(max_length=128)
    std_stable1 = models.IntegerField()
    std_stable2 = models.IntegerField()
    std_arbor = models.IntegerField()
    stable1 = models.IntegerField()
    stable2 = models.IntegerField()
    arbor = models.IntegerField()
    gravit = models.IntegerField()
    remarks = models.CharField(max_length=200)
    financial_approval = models.BooleanField()
    procurement_approval = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_name

    class Meta:
        db_table = "project_planner_data"


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
