from rest_framework.routers import SimpleRouter

from .views import Hospital_ModelViewSet
from .views import Material_ModelViewSet
from .views import Staff_ModelViewSet
from .views import Hospital_Location_ModelViewSet
from .views import Point_Forecast_Records_ModelViewSet
from .views import Points_Message_ModelViewSet
from .views import Points_Establish_ModelViewSet
from .views import Hospital_to_Material_ModelViewSet
from .views import Hospital_to_Staff_ModelViewSet
from .views import Hospital_to_Hospital_Location_ModelViewSet
from .views import Points_Establish_to_Points_Location_ModelViewSet
from .views import Points_Location_to_Points_Message_ModelViewSet
from .views import Data_ModelViewSet
from .views import Epidemic_situation_ModelViewSet
from .views import Level_ModelViewSet
from .views import Epidemic_situation_Location_ModelViewSet
from .views import Epidemic_situation_Message_ModelViewSet
from .views import Emergency_dispatch_Need_ModelViewSet
from .views import Epidemic_situation_Location_to_Epidemic_situation_Message_ModelViewSet
from .views import Epidemic_situation_to_Epidemic_situation_Location_ModelViewSet
from .views import Level_to_Epidemic_situation_ModelViewSet
from .views import Default_Point_ModelViewSet
# from .views import jiekouceshi


router = SimpleRouter()
router.register("/Data_ModelView",Data_ModelViewSet)
router.register("/Epidemic_situation_ModelView",Epidemic_situation_ModelViewSet)
router.register("/Level_ModelView",Level_ModelViewSet)
router.register("/Epidemic_situation_Location_ModelView",Epidemic_situation_Location_ModelViewSet)
router.register("/Epidemic_situation_Message_ModelView",Epidemic_situation_Message_ModelViewSet)
router.register("/Emergency_dispatch_Need_ModelView",Emergency_dispatch_Need_ModelViewSet)
router.register("/Epidemic_situation_Location_to_Epidemic_situation_Message_ModelView",Epidemic_situation_Location_to_Epidemic_situation_Message_ModelViewSet)
router.register("/Epidemic_situation_to_Epidemic_situation_Location_ModelView",Epidemic_situation_to_Epidemic_situation_Location_ModelViewSet)
router.register("/Level_to_Epidemic_situation_ModelView",Level_to_Epidemic_situation_ModelViewSet)


router.register("/Default_Point_Model",Default_Point_ModelViewSet)
router.register("/Hospital_Model",Hospital_ModelViewSet)
router.register("/Material_Model",Material_ModelViewSet)
router.register("/Staff_Model",Staff_ModelViewSet)
router.register("/Hospital_Location_Model",Hospital_Location_ModelViewSet)
router.register("/Point_Forecast_Records_Model",Point_Forecast_Records_ModelViewSet)
router.register("/Points_Message_Model",Points_Message_ModelViewSet)
router.register("/Points_Establish_Model",Points_Establish_ModelViewSet)
router.register("/Hospital_to_Material_Model",Hospital_to_Material_ModelViewSet)
router.register("/Hospital_to_Staff_Model",Hospital_to_Staff_ModelViewSet)
router.register("/Hospital_to_Hospital_Location_Model",Hospital_to_Hospital_Location_ModelViewSet)
router.register("/Points_Establish_to_Points_Location_Model",Points_Establish_to_Points_Location_ModelViewSet)
router.register("/Points_Location_to_Points_Message_Model",Points_Location_to_Points_Message_ModelViewSet)

# router.register("/test",jiekouceshi)

urlpatterns = []
urlpatterns += router.urls