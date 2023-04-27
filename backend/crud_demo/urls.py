from rest_framework.routers import SimpleRouter

from .views import CrudDemoModelViewSet

router = SimpleRouter()
router.register("", CrudDemoModelViewSet)

urlpatterns = [
]
urlpatterns += router.urls