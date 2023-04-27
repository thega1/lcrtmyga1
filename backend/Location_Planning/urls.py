from rest_framework.routers import SimpleRouter

router = SimpleRouter
router.register("api/Location_Planning")

urlpatterns = [
]
urlpatterns += router.urls