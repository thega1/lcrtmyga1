from Nucleic_acid_testing.models import Hospital_Model
from Nucleic_acid_testing.models import Material_Model
from Nucleic_acid_testing.models import Staff_Model
from Nucleic_acid_testing.models import Hospital_Location_Model
from Nucleic_acid_testing.models import Point_Forecast_Records_Model
from Nucleic_acid_testing.models import Points_Message_Model
from Nucleic_acid_testing.models import Points_Establish_Model
from Nucleic_acid_testing.models import Hospital_to_Material_Model
from Nucleic_acid_testing.models import Hospital_to_Staff_Model
from Nucleic_acid_testing.models import Hospital_to_Hospital_Location_Model
from Nucleic_acid_testing.models import Points_Establish_to_Points_Location_Model
from Nucleic_acid_testing.models import Points_Location_to_Points_Message_Model
from Nucleic_acid_testing.models import Default_Point_Model

from Nucleic_acid_testing.models import Data_Model
from Nucleic_acid_testing.models import Epidemic_situation_Model
from Nucleic_acid_testing.models import Level_Model
from Nucleic_acid_testing.models import Epidemic_situation_Location_Model
from Nucleic_acid_testing.models import Epidemic_situation_Message_Model
from Nucleic_acid_testing.models import Emergency_dispatch_Need_Model
from Nucleic_acid_testing.models import Epidemic_situation_Location_to_Epidemic_situation_Message_Model
from Nucleic_acid_testing.models import Epidemic_situation_to_Epidemic_situation_Location_Model
from Nucleic_acid_testing.models import Level_to_Epidemic_situation_Model


from dvadmin.utils.serializers import CustomModelSerializer


# Default_Point_Model
class Default_Point_ModelSerializer(CustomModelSerializer):

    class Meta:
        model = Default_Point_Model
        fields = "__all__"

class Default_Point_ModelCreateUpdateSerializer(CustomModelSerializer):

    class Meta:
        model = Default_Point_Model
        fields = "__all__"

# Point_Forecast_Records_Model
class Point_Forecast_Records_ModelSerializer(CustomModelSerializer):

    class Meta:
        model = Point_Forecast_Records_Model
        fields = "__all__"

class Point_Forecast_Records_ModelCreateUpdateSerializer(CustomModelSerializer):

    class Meta:
        model = Point_Forecast_Records_Model
        fields = "__all__"


# Hospital_Model的序列化器与反序列化器
class Hospital_ModelSerializer(CustomModelSerializer):

    class Meta:
        model = Hospital_Model
        fields = "__all__"

class Hospital_ModelCreateUpdateSerializer(CustomModelSerializer):

    class Meta:
        model = Hospital_Model
        fields = "__all__"


# Material_Model
class Material_ModelSerializer(CustomModelSerializer):
    class Meta:
        model = Material_Model
        fields = "__all__"

class Material_ModelCreateUpdateSerializer(CustomModelSerializer):
    class Meta:
        model = Material_Model
        fields = "__all__"

# Staff_Model
class Staff_ModelSerializer(CustomModelSerializer):
    class Meta:
        model = Staff_Model
        fields = "__all__"

class Staff_ModelCreateUpdateSerializer(CustomModelSerializer):
    class Meta:
        model = Staff_Model
        fields = "__all__"

# Hospital_Location_Model
class Hospital_Location_ModelSerializer(CustomModelSerializer):
    class Meta:
        model = Hospital_Location_Model
        fields = "__all__"

class Hospital_Location_ModelCreateUpdateSerializer(CustomModelSerializer):
    class Meta:
        model = Hospital_Location_Model
        fields = "__all__"

# Points_Message_Model
# class Points_Message_ModelSerializer(CustomModelSerializer):
#     class Meta:
#         model = Points_Message_Model
#         fields = "__all__"
#
# class Points_Message_ModelCreateUpdateSerializer(CustomModelSerializer):
#     class Meta:
#         model = Points_Message_Model
#         fields = "__all__"

# Points_Message_Model
class Points_Message_ModelSerializer(CustomModelSerializer):
    class Meta:
        model = Points_Message_Model
        fields = "__all__"

class Points_Message_ModelCreateUpdateSerializer(CustomModelSerializer):
    class Meta:
        model = Points_Message_Model
        fields = "__all__"

# Points_Establish_Model
class Points_Establish_ModelSerializer(CustomModelSerializer):
    class Meta:
        model = Points_Establish_Model
        fields = "__all__"

class Points_Establish_ModelCreateUpdateSerializer(CustomModelSerializer):
    class Meta:
        model = Points_Establish_Model
        fields = "__all__"

# Hospital_to_Material_Model
class Hospital_to_Material_ModelSerializer(CustomModelSerializer):
    class Meta:
        model = Hospital_to_Material_Model
        fields = "__all__"

class Hospital_to_Material_ModelCreateUpdateSerializer(CustomModelSerializer):
    class Meta:
        model = Hospital_to_Material_Model
        fields = "__all__"

# Hospital_to_Staff_Model
class Hospital_to_Staff_ModelSerializer(CustomModelSerializer):
    class Meta:
        model = Hospital_to_Staff_Model
        fields = "__all__"

class Hospital_to_Staff_ModelCreateUpdateSerializer(CustomModelSerializer):
    class Meta:
        model = Hospital_to_Staff_Model
        fields = "__all__"

# Hospital_to_Hospital_Location_Model
class Hospital_to_Hospital_Location_ModelSerializer(CustomModelSerializer):
    class Meta:
        model = Hospital_to_Hospital_Location_Model
        fields = "__all__"

class Hospital_to_Hospital_Location_ModelCreateUpdateSerializer(CustomModelSerializer):
    class Meta:
        model = Hospital_to_Hospital_Location_Model
        fields = "__all__"

# Points_Establish_to_Points_Location_Model
class Points_Establish_to_Points_Location_ModelSerializer(CustomModelSerializer):
    class Meta:
        model = Points_Establish_to_Points_Location_Model
        fields = "__all__"

class Points_Establish_to_Points_Location_ModelCreateUpdateSerializer(CustomModelSerializer):
    class Meta:
        model = Points_Establish_to_Points_Location_Model
        fields = "__all__"

# Points_Location_to_Points_Message_Model
class Points_Location_to_Points_Message_ModelSerializer(CustomModelSerializer):
    class Meta:
        model = Points_Location_to_Points_Message_Model
        fields = "__all__"

class Points_Location_to_Points_Message_ModelCreateUpdateSerializer(CustomModelSerializer):
    class Meta:
        model = Points_Location_to_Points_Message_Model
        fields = "__all__"




# Data
class Data_ModelSerializer(CustomModelSerializer):
    class Meta:
        model = Data_Model
        fields = "__all__"


class Data_ModelCreateUpdateSerializer(CustomModelSerializer):
    class Meta:
        model = Data_Model
        fields = "__all__"


# Epidemic_situation_Model
class Epidemic_situation_ModelSerializer(CustomModelSerializer):
    class Meta:
        model = Epidemic_situation_Model
        fields = "__all__"


class Epidemic_situation_ModelCreateUpdateSerializer(CustomModelSerializer):
    class Meta:
        model = Epidemic_situation_Model
        fields = "__all__"


# Level_Model
class Level_ModelSerializer(CustomModelSerializer):
    class Meta:
        model = Level_Model
        fields = "__all__"


class Level_ModelCreateUpdateSerializer(CustomModelSerializer):
    class Meta:
        model = Level_Model
        fields = "__all__"


# Epidemic_situation_Location_Model
class Epidemic_situation_Location_ModelSerializer(CustomModelSerializer):
    class Meta:
        model = Epidemic_situation_Location_Model
        fields = "__all__"


class Epidemic_situation_Location_ModelCreateUpdateSerializer(CustomModelSerializer):
    class Meta:
        model = Epidemic_situation_Location_Model
        fields = "__all__"


# Epidemic_situation_Message_Model
class Epidemic_situation_Message_ModelSerializer(CustomModelSerializer):
    class Meta:
        model = Epidemic_situation_Message_Model
        fields = "__all__"


class Epidemic_situation_Message_ModelCreateUpdateSerializer(CustomModelSerializer):
    class Meta:
        model = Epidemic_situation_Message_Model
        fields = "__all__"


# Emergency_dispatch_Need_Model
class Emergency_dispatch_Need_ModelSerializer(CustomModelSerializer):
    class Meta:
        model = Emergency_dispatch_Need_Model
        fields = "__all__"


class Emergency_dispatch_Need_ModelCreateUpdateSerializer(CustomModelSerializer):
    class Meta:
        model = Emergency_dispatch_Need_Model
        fields = "__all__"


# Epidemic_situation_Location_to_Epidemic_situation_Message_Model
class Epidemic_situation_Location_to_Epidemic_situation_Message_ModelSerializer(CustomModelSerializer):
    class Meta:
        model = Epidemic_situation_Location_to_Epidemic_situation_Message_Model
        fields = "__all__"


class Epidemic_situation_Location_to_Epidemic_situation_Message_ModelCreateUpdateSerializer(CustomModelSerializer):
    class Meta:
        model = Epidemic_situation_Location_to_Epidemic_situation_Message_Model
        fields = "__all__"


# Epidemic_situation_to_Epidemic_situation_Location_Model
class Epidemic_situation_to_Epidemic_situation_Location_ModelSerializer(CustomModelSerializer):
    class Meta:
        model = Epidemic_situation_to_Epidemic_situation_Location_Model
        fields = "__all__"


class Epidemic_situation_to_Epidemic_situation_Location_ModelCreateUpdateSerializer(CustomModelSerializer):
    class Meta:
        model = Epidemic_situation_to_Epidemic_situation_Location_Model
        fields = "__all__"


# Level_to_Epidemic_situation_Model
class Level_to_Epidemic_situation_ModelSerializer(CustomModelSerializer):
    class Meta:
        model = Level_to_Epidemic_situation_Model
        fields = "__all__"


class Level_to_Epidemic_situation_ModelCreateUpdateSerializer(CustomModelSerializer):
    class Meta:
        model = Level_to_Epidemic_situation_Model
        fields = "__all__"

