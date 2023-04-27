from django.shortcuts import render

from Nucleic_acid_testing.models import Hospital_Model
from Nucleic_acid_testing.models import Material_Model
from Nucleic_acid_testing.models import Staff_Model
from Nucleic_acid_testing.models import Hospital_Location_Model
from Nucleic_acid_testing.models import Points_Message_Model
from Nucleic_acid_testing.models import Points_Establish_Model
from Nucleic_acid_testing.models import Hospital_to_Material_Model
from Nucleic_acid_testing.models import Hospital_to_Staff_Model
from Nucleic_acid_testing.models import Hospital_to_Hospital_Location_Model
from Nucleic_acid_testing.models import Points_Establish_to_Points_Location_Model
from Nucleic_acid_testing.models import Points_Location_to_Points_Message_Model

from Nucleic_acid_testing.models import Data_Model
from Nucleic_acid_testing.models import Epidemic_situation_Model
from Nucleic_acid_testing.models import Level_Model
from Nucleic_acid_testing.models import Epidemic_situation_Location_Model
from Nucleic_acid_testing.models import Epidemic_situation_Message_Model
from Nucleic_acid_testing.models import Emergency_dispatch_Need_Model
from Nucleic_acid_testing.models import Epidemic_situation_Location_to_Epidemic_situation_Message_Model
from Nucleic_acid_testing.models import Epidemic_situation_to_Epidemic_situation_Location_Model
from Nucleic_acid_testing.models import Level_to_Epidemic_situation_Model
from Nucleic_acid_testing.models import Point_Forecast_Records_Model
from Nucleic_acid_testing.models import Default_Point_Model



from Nucleic_acid_testing.serializer import Default_Point_ModelSerializer,Default_Point_ModelCreateUpdateSerializer
from Nucleic_acid_testing.serializer import Hospital_ModelSerializer,Hospital_ModelCreateUpdateSerializer
from Nucleic_acid_testing.serializer import Material_ModelSerializer,Material_ModelCreateUpdateSerializer
from Nucleic_acid_testing.serializer import Staff_ModelSerializer,Staff_ModelCreateUpdateSerializer
from Nucleic_acid_testing.serializer import Hospital_Location_ModelSerializer,Hospital_Location_ModelCreateUpdateSerializer
from Nucleic_acid_testing.serializer import Point_Forecast_Records_ModelSerializer,Point_Forecast_Records_ModelCreateUpdateSerializer
from Nucleic_acid_testing.serializer import Points_Message_ModelSerializer,Points_Message_ModelCreateUpdateSerializer
from Nucleic_acid_testing.serializer import Points_Establish_ModelSerializer,Points_Establish_ModelCreateUpdateSerializer
from Nucleic_acid_testing.serializer import Hospital_to_Material_ModelSerializer,Hospital_to_Material_ModelCreateUpdateSerializer
from Nucleic_acid_testing.serializer import Hospital_to_Staff_ModelSerializer,Hospital_to_Staff_ModelCreateUpdateSerializer
from Nucleic_acid_testing.serializer import Hospital_to_Hospital_Location_ModelSerializer,Hospital_to_Hospital_Location_ModelCreateUpdateSerializer
from Nucleic_acid_testing.serializer import Points_Establish_to_Points_Location_ModelSerializer,Points_Establish_to_Points_Location_ModelCreateUpdateSerializer
from Nucleic_acid_testing.serializer import Points_Location_to_Points_Message_ModelSerializer,Points_Location_to_Points_Message_ModelCreateUpdateSerializer

from Nucleic_acid_testing.serializer import Data_ModelSerializer,Data_ModelCreateUpdateSerializer
from Nucleic_acid_testing.serializer import Epidemic_situation_ModelSerializer,Epidemic_situation_ModelCreateUpdateSerializer
from Nucleic_acid_testing.serializer import Level_ModelSerializer,Level_ModelCreateUpdateSerializer
from Nucleic_acid_testing.serializer import Epidemic_situation_Location_ModelSerializer,Epidemic_situation_Location_ModelCreateUpdateSerializer
from Nucleic_acid_testing.serializer import Epidemic_situation_Message_ModelSerializer,Epidemic_situation_Message_ModelCreateUpdateSerializer
from Nucleic_acid_testing.serializer import Emergency_dispatch_Need_ModelSerializer,Emergency_dispatch_Need_ModelCreateUpdateSerializer
from Nucleic_acid_testing.serializer import Epidemic_situation_Location_to_Epidemic_situation_Message_ModelSerializer,Epidemic_situation_Location_to_Epidemic_situation_Message_ModelCreateUpdateSerializer
from Nucleic_acid_testing.serializer import Epidemic_situation_to_Epidemic_situation_Location_ModelSerializer,Epidemic_situation_to_Epidemic_situation_Location_ModelCreateUpdateSerializer
from Nucleic_acid_testing.serializer import Level_to_Epidemic_situation_ModelSerializer,Level_to_Epidemic_situation_ModelCreateUpdateSerializer

from dvadmin.utils.viewset import CustomModelViewSet
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound
# Create your views here.

# Point_Forecast_Records_ModelSerializer
class Point_Forecast_Records_ModelViewSet(CustomModelViewSet):
    queryset = Point_Forecast_Records_Model.objects.all()
    serializer_class = Point_Forecast_Records_ModelSerializer
    create_serializer_class = Point_Forecast_Records_ModelCreateUpdateSerializer
    update_serializer_class = Point_Forecast_Records_ModelCreateUpdateSerializer

# Default_Point_Model
class Default_Point_ModelViewSet(CustomModelViewSet):
    queryset = Default_Point_Model.objects.all()
    serializer_class = Default_Point_ModelSerializer
    create_serializer_class = Default_Point_ModelCreateUpdateSerializer
    update_serializer_class = Default_Point_ModelCreateUpdateSerializer


class Hospital_ModelViewSet(CustomModelViewSet):
    queryset = Hospital_Model.objects.all()
    serializer_class = Hospital_ModelSerializer
    create_serializer_class = Hospital_ModelCreateUpdateSerializer
    update_serializer_class = Hospital_ModelCreateUpdateSerializer
    filter_fields = ['name','postion']
    search_fields = ['name']


# Material_Model
class Material_ModelViewSet(CustomModelViewSet):
    queryset = Material_Model.objects.all()
    serializer_class = Material_ModelSerializer
    create_serializer_class = Material_ModelCreateUpdateSerializer

    update_serializer_class = Material_ModelCreateUpdateSerializer


# Staff_Model
class Staff_ModelViewSet(CustomModelViewSet):
    queryset = Staff_Model.objects.all()
    serializer_class = Staff_ModelSerializer
    create_serializer_class = Staff_ModelCreateUpdateSerializer
    update_serializer_class = Staff_ModelCreateUpdateSerializer

# Hospital_Location_Model
class Hospital_Location_ModelViewSet(CustomModelViewSet):
    queryset = Hospital_Location_Model.objects.all()
    serializer_class = Hospital_Location_ModelSerializer
    create_serializer_class = Hospital_Location_ModelCreateUpdateSerializer
    update_serializer_class = Hospital_Location_ModelCreateUpdateSerializer



# Points_Location_Model
# class Points_Location_ModelViewSet(CustomModelViewSet):
#     queryset = Points_Message_Model.objects.all()
#     serializer_class = Points_Location_ModelSerializer
#     create_serializer_class = Points_Location_ModelCreateUpdateSerializer
#     update_serializer_class = Points_Location_ModelCreateUpdateSerializer

# Points_Message_Model
class Points_Message_ModelViewSet(CustomModelViewSet):
    queryset = Points_Message_Model.objects.all()
    serializer_class = Points_Message_ModelSerializer
    create_serializer_class = Points_Message_ModelCreateUpdateSerializer
    update_serializer_class = Points_Message_ModelCreateUpdateSerializer

# Points_Establish_Model
class Points_Establish_ModelViewSet(CustomModelViewSet):
    queryset = Points_Establish_Model.objects.all()
    serializer_class = Points_Establish_ModelSerializer
    create_serializer_class = Points_Establish_ModelCreateUpdateSerializer
    update_serializer_class = Points_Establish_ModelCreateUpdateSerializer

# Hospital_to_Material_Model
class Hospital_to_Material_ModelViewSet(CustomModelViewSet):
    queryset = Hospital_to_Material_Model.objects.all()
    serializer_class = Hospital_to_Material_ModelSerializer
    create_serializer_class = Hospital_to_Material_ModelCreateUpdateSerializer
    update_serializer_class = Hospital_to_Material_ModelCreateUpdateSerializer

# Hospital_to_Staff_Model
class Hospital_to_Staff_ModelViewSet(CustomModelViewSet):
    queryset = Hospital_to_Staff_Model.objects.all()
    serializer_class = Hospital_to_Staff_ModelSerializer
    create_serializer_class = Hospital_to_Staff_ModelCreateUpdateSerializer
    update_serializer_class = Hospital_to_Staff_ModelCreateUpdateSerializer

# Hospital_to_Hospital_Location_Model
class Hospital_to_Hospital_Location_ModelViewSet(CustomModelViewSet):
    queryset = Hospital_to_Hospital_Location_Model.objects.all()
    serializer_class = Hospital_to_Hospital_Location_ModelSerializer
    create_serializer_class = Hospital_to_Hospital_Location_ModelCreateUpdateSerializer
    update_serializer_class = Hospital_to_Hospital_Location_ModelCreateUpdateSerializer

# Points_Establish_to_Points_Location_Model
class Points_Establish_to_Points_Location_ModelViewSet(CustomModelViewSet):
    queryset = Points_Establish_to_Points_Location_Model.objects.all()
    serializer_class = Points_Establish_to_Points_Location_ModelSerializer
    create_serializer_class = Points_Establish_to_Points_Location_ModelCreateUpdateSerializer
    update_serializer_class = Points_Establish_to_Points_Location_ModelCreateUpdateSerializer

# Points_Location_to_Points_Message_Model
class Points_Location_to_Points_Message_ModelViewSet(CustomModelViewSet):
    queryset = Points_Location_to_Points_Message_Model.objects.all()
    serializer_class = Points_Location_to_Points_Message_ModelSerializer
    create_serializer_class = Points_Location_to_Points_Message_ModelCreateUpdateSerializer
    update_serializer_class = Points_Location_to_Points_Message_ModelCreateUpdateSerializer


# kaishi

class Data_ModelViewSet(CustomModelViewSet):
    queryset = Data_Model.objects.all()
    serializer_class = Data_ModelSerializer
    create_serializer_class = Data_ModelCreateUpdateSerializer
    update_serializer_class = Data_ModelCreateUpdateSerializer


# Epidemic_situation_Model
class Epidemic_situation_ModelViewSet(CustomModelViewSet):
    queryset = Epidemic_situation_Model.objects.all()
    serializer_class = Epidemic_situation_ModelSerializer
    create_serializer_class = Epidemic_situation_ModelCreateUpdateSerializer
    update_serializer_class = Epidemic_situation_ModelCreateUpdateSerializer


# Level_Model
class Level_ModelViewSet(CustomModelViewSet):
    queryset = Level_Model.objects.all()
    serializer_class = Level_ModelSerializer
    create_serializer_class = Level_ModelCreateUpdateSerializer
    update_serializer_class = Level_ModelCreateUpdateSerializer


# Epidemic_situation_Location_Model
class Epidemic_situation_Location_ModelViewSet(CustomModelViewSet):
    queryset = Epidemic_situation_Location_Model.objects.all()
    serializer_class = Epidemic_situation_Location_ModelSerializer
    create_serializer_class = Epidemic_situation_Location_ModelCreateUpdateSerializer
    update_serializer_class = Epidemic_situation_Location_ModelCreateUpdateSerializer


# Epidemic_situation_Message_Model
class Epidemic_situation_Message_ModelViewSet(CustomModelViewSet):
    queryset = Epidemic_situation_Message_Model.objects.all()
    serializer_class = Epidemic_situation_Message_ModelSerializer
    create_serializer_class = Epidemic_situation_Message_ModelCreateUpdateSerializer
    update_serializer_class = Epidemic_situation_Message_ModelCreateUpdateSerializer


# Emergency_dispatch_Need_Model
class Emergency_dispatch_Need_ModelViewSet(CustomModelViewSet):
    queryset = Emergency_dispatch_Need_Model.objects.all()
    serializer_class = Emergency_dispatch_Need_ModelSerializer
    create_serializer_class = Emergency_dispatch_Need_ModelCreateUpdateSerializer
    update_serializer_class = Emergency_dispatch_Need_ModelCreateUpdateSerializer


# Epidemic_situation_Location_to_Epidemic_situation_Message_Model
class Epidemic_situation_Location_to_Epidemic_situation_Message_ModelViewSet(CustomModelViewSet):
    queryset = Epidemic_situation_Location_to_Epidemic_situation_Message_Model.objects.all()
    serializer_class = Epidemic_situation_Location_to_Epidemic_situation_Message_ModelSerializer
    create_serializer_class = Epidemic_situation_Location_to_Epidemic_situation_Message_ModelCreateUpdateSerializer
    update_serializer_class = Epidemic_situation_Location_to_Epidemic_situation_Message_ModelCreateUpdateSerializer


# Epidemic_situation_to_Epidemic_situation_Location_Model
class Epidemic_situation_to_Epidemic_situation_Location_ModelViewSet(CustomModelViewSet):
    queryset = Epidemic_situation_to_Epidemic_situation_Location_Model.objects.all()
    serializer_class = Epidemic_situation_to_Epidemic_situation_Location_ModelSerializer
    create_serializer_class = Epidemic_situation_to_Epidemic_situation_Location_ModelCreateUpdateSerializer
    update_serializer_class = Epidemic_situation_to_Epidemic_situation_Location_ModelCreateUpdateSerializer


# Level_to_Epidemic_situation_Model
class Level_to_Epidemic_situation_ModelViewSet(CustomModelViewSet):
    queryset = Level_to_Epidemic_situation_Model.objects.all()
    serializer_class = Level_to_Epidemic_situation_ModelSerializer
    create_serializer_class = Level_to_Epidemic_situation_ModelCreateUpdateSerializer
    update_serializer_class = Level_to_Epidemic_situation_ModelCreateUpdateSerializer

# class Test_ViewSet():

# jieshu

# 获取预测前核酸检测点信息
def point_message(request):
    result=Default_Point_Model.objects.all()
    data = []
    for i in result:
        ziduan = ['name','show','markerPoint']
        zhi = []
        zhi.append(i.name)
        zhi.append(False)
        markerPoint = {"lng":i.jingdu,"lat":i.weidu}
        zhi.append(markerPoint)
        onedata = dict(zip(ziduan,zhi))
        data.append(onedata)
    # print("="*30)
    # print(data)
    # print("="*30)
    data = {'data':data}
    return JsonResponse(data)

# 获取预测后核酸检测点结果
def point_result(request):
    result=Points_Message_Model.objects.all()
    data = []
    for i in result:
        ziduan = ['name','show','markerPoint']
        zhi = []
        zhi.append(i.name)
        zhi.append(False)
        markerPoint = {"lng":i.jingdu,"lat":i.weidu}
        zhi.append(markerPoint)
        onedata = dict(zip(ziduan,zhi))
        data.append(onedata)
    # print("="*30)
    # print(data)
    # print("="*30)
    data = {'data':data}
    return JsonResponse(data)



