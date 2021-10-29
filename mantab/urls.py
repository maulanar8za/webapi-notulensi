from rest_framework.routers import DefaultRouter
from .views import AsistenViewSet
from django.urls import path,include

app_name='mantab'

router = DefaultRouter()
router.register('mantab',AsistenViewSet)

urlpatterns = [
    path ('api/',include(router.urls)),
]