from django.db import models

# Create your models here.
from dvadmin.utils.models import CoreModel

class Hospital_Model(CoreModel):
    name = models.CharField(max_length=255,verbose_name="医院名称")
    # postion = models.CharField(max_length=255,verbose_name="医院位置")
    jingdu = models.FloatField(verbose_name="医院经度",default=0)
    weidu = models.FloatField(verbose_name="医院纬度",default=0)
    class Meta:
        db_table = "Hospital"
        verbose_name = "医院表"

class Material_Model(CoreModel):
    name = models.CharField(max_length=255,verbose_name="物资名称")
    num = models.IntegerField(verbose_name="物资库存")
    belong = models.CharField(max_length=255,verbose_name="所属医院",default="")

    class Meta:
        db_table = "Material"
        verbose_name = "物资表"

class Staff_Model(CoreModel):
    name = models.CharField(max_length=255,verbose_name="姓名")
    identity = models.CharField(max_length=255,verbose_name="身份")
    belong = models.CharField(max_length=255,verbose_name="所属医院",default="")
    class Meta:
        db_table = "Staff"
        verbose_name = "人员表"

class Hospital_Location_Model(CoreModel):
    # location = models.CharField(max_length=255,verbose_name="经纬度")
    jingdu = models.FloatField(verbose_name="医院经度", default=0)
    weidu = models.FloatField(verbose_name="医院纬度", default=0)
    name = models.CharField(max_length=255, verbose_name="医院名称",default="")
    class Meta:
        db_table = "Hospital_Location"
        verbose_name = "医院位置表"

# 新增
class Default_Point_Model(CoreModel):
    name = models.CharField(max_length=255,verbose_name="核酸检测点名称")
    nearest = models.IntegerField(verbose_name="首近医院距离")
    nearer = models.IntegerField(verbose_name="次近医院距离")
    population_density = models.IntegerField(verbose_name="人口密度")
    population_flow = models.IntegerField(verbose_name="人口流量")
    jingdu = models.FloatField(verbose_name="预设核酸检测点经度",default=0)
    weidu = models.FloatField(verbose_name="预设核酸检测点纬度",default=0)
    class Meta:
        db_table = "Default_Point"
        verbose_name = "预设核酸检测点表"

class Points_Message_Model(CoreModel):
    jingdu = models.FloatField(verbose_name="检测点经度", default=0)
    weidu = models.FloatField(verbose_name="检测点纬度", default=0)
    name = models.CharField(max_length=255,verbose_name="检测点名称")
    box = models.IntegerField(verbose_name="生物试验箱数量",default=0)
    shizi = models.IntegerField(verbose_name="拭子数量",default=0)
    shiguan = models.IntegerField(verbose_name="试管数量",default=0)
    class Meta:
        db_table = "Points_Message"
        verbose_name = "核酸检测点信息表"

class Material_Distribution_Records_Model(CoreModel):
    name = models.CharField(max_length=255,verbose_name="检测点名称",default="NUll")
    person_number = models.IntegerField(verbose_name="人员数量")
    box = models.IntegerField(verbose_name="生物箱数量")
    cuvette = models.IntegerField(verbose_name="试管数量")
    swab = models.IntegerField(verbose_name="拭子数量")
    class Meta:
        db_table = 'Material_Distribution_Records'
        verbose_name = "物资分配记录表"

# 新增
class Point_Forecast_Records_Model(CoreModel):
    name = models.CharField(max_length=255,verbose_name="核酸检测点名称")
    jingdu = models.FloatField(verbose_name="检测点经度",default=0)
    weidu = models.FloatField(verbose_name="检测点纬度",default=0)
    class Meta:
        db_table = "Point_Forecast_Records"
        verbose_name = "核酸检测点预测记录表"

class Points_Establish_Model(CoreModel):
    name = models.CharField(max_length=255,verbose_name="确立检测点名称")
    nearest = models.IntegerField(verbose_name="首近医院距离")
    nearer = models.IntegerField(verbose_name="次近医院距离")
    population_density = models.IntegerField(verbose_name="人口密度")
    population_flow = models.IntegerField(verbose_name="人口流量")

    class Meta:
        db_table = 'Points_Establish'
        verbose_name = "核酸检测点确立"

class Hospital_to_Material_Model(CoreModel):
    q_id = models.IntegerField(verbose_name="医院id")
    h_id = models.IntegerField(verbose_name="物资id")

    class Meta:
        db_table = 'Hospital_to_Material'
        verbose_name = "医院、物资关联表"


class Hospital_to_Staff_Model(CoreModel):
    q_id = models.IntegerField(verbose_name="医院id")
    h_id = models.IntegerField(verbose_name="人员id")

    class Meta:
        db_table = 'Hospital_to_Staff'
        verbose_name = "医院、人员关联表"

class Hospital_to_Hospital_Location_Model(CoreModel):
    q_id = models.IntegerField(verbose_name="医院id")
    h_id = models.IntegerField(verbose_name="医院位置id")

    class Meta:
        db_table = 'Hospital_to_Hospital_Location'
        verbose_name = "医院、位置关联表"

class Points_Establish_to_Points_Location_Model(CoreModel):
    q_id = models.IntegerField(verbose_name="检测点确立id")
    h_id = models.IntegerField(verbose_name="检测点位置id")
    class Meta:
        db_table = 'Points_Establish_to_Points_Location'
        verbose_name = "核酸检测点确立、核酸检测点位置关联表"

class Points_Location_to_Points_Message_Model(CoreModel):
    q_id = models.IntegerField(verbose_name="检测点位置id")
    h_id = models.IntegerField(verbose_name="检测点信息id")
    class Meta:
        db_table = 'Points_Location_to_Points_Message'
        verbose_name = "核酸检测点位置、核酸检测点信息关联表"

# 与核酸检测点确立表相关联
class Data_Model(CoreModel):
    num = models.IntegerField(verbose_name="人员数量")
    name = models.CharField(max_length=255, verbose_name="确立检测点名称")
    nearest = models.IntegerField(verbose_name="首近医院距离")
    nearer = models.IntegerField(verbose_name="次近医院距离")
    population_density = models.IntegerField(verbose_name="人口密度")
    population_flow = models.IntegerField(verbose_name="人口流量")
    class Meta:
        db_table = 'data'
        verbose_name = "模型数据表"

class Epidemic_situation_Model(CoreModel):
    num = models.IntegerField(verbose_name="感染人数")
    level = models.IntegerField(verbose_name="封控等级")
    population_density = models.IntegerField(verbose_name="人口密度")
    population_flow = models.IntegerField(verbose_name="人口流量")
    class Meta:
        db_table = "Epidemic_situation"
        verbose_name = "疫情表"

class Level_Model(CoreModel):
    trip = models.IntegerField(verbose_name="行程范围")
    live = models.IntegerField(verbose_name="居住范围")
    level = models.IntegerField(verbose_name="封控等级")
    class Meta:
        db_table = "Level"
        verbose_name = "封控等级表"

class Epidemic_situation_Location_Model(CoreModel):
    postion = models.CharField(max_length=255,verbose_name="经纬度")
    class Meta:
        db_table = "Epidemic_situation_Location"
        verbose_name = "疫情位置表"

class Epidemic_situation_Message_Model(CoreModel):
    nearest = models.IntegerField(verbose_name="首近医院距离")
    nearer = models.IntegerField(verbose_name="次近医院距离")
    class Meta:
        db_table = "Epidemic_situation_Message"
        verbose_name = "疫情信息表"

class Emergency_dispatch_Need_Model(CoreModel):
    doctor_num = models.IntegerField(verbose_name="医生数量")
    volunteer_num = models.IntegerField(verbose_name="志愿者数量")
    cuvette_num = models.IntegerField(verbose_name="试管数量")
    swab_num = models.IntegerField(verbose_name="拭子数量")
    box_num = models.IntegerField(verbose_name="生物转移箱数量")
    class Meta:
        db_table = "Emergency_dispatch_Need"
        verbose_name = "紧急调度所需资源表"

class Epidemic_situation_Location_to_Epidemic_situation_Message_Model(CoreModel):
    q_id = models.IntegerField(verbose_name="疫情位置id")
    h_id = models.IntegerField(verbose_name="疫情信息id")
    class Meta:
        db_table = "Epidemic_situation_Location_to_Epidemic_situation_Message"
        verbose_name = "疫情位置与疫情信息关联表"

class Epidemic_situation_to_Epidemic_situation_Location_Model(CoreModel):
    q_id = models.IntegerField(verbose_name="疫情id")
    h_id = models.IntegerField(verbose_name="疫情位置id")
    class Meta:
        db_table = "Epidemic_situation_to_Epidemic_situation_Location"
        verbose_name = "疫情与疫情位置关联表"

class Level_to_Epidemic_situation_Model(CoreModel):
    q_id = models.IntegerField(verbose_name="疫情id")
    level = models.IntegerField(verbose_name="封控等级")
    class Meta:
        db_table = "Level_to_Epidemic_situation"
        verbose_name = "封控等级与疫情关联表"


class Point_Predic_Outcome(CoreModel):
    name = models.CharField(max_length=255,verbose_name="确定核酸检测点名称")
    jingdu = models.FloatField(verbose_name="确定核酸检测点经度")
    weidu = models.FloatField(verbose_name="确定核酸检测点纬度")
    class Meta:
        db_table = "Point_Predic"
        verbose_name = "核酸检测点预测结果"

