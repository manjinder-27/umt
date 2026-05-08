from django.db import models
from django.contrib.auth.models import User

class Monitor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,editable=False)
    name = models.CharField(max_length=120)
    url = models.URLField()
    interval = models.IntegerField()
    expected_status = models.IntegerField()
    status = models.CharField(max_length=9,null=True)
    latency = models.CharField(max_length=9,null=True)