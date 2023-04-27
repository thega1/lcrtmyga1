from django.db import models

# Create your models here.
from dvadmin.utils.models import CoreModel

class PointforecaseModel(CoreModel):
    name = models.CharField(max_length=255,verbose_name="预设核酸检测点名称")
    location = models.CharField(max_length=255,verbose_name="预设核酸检测点位置")
    distance = models.FloatField(verbose_name="核酸检测点距离医院1的距离0")
