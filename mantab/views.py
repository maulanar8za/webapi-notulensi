from rest_framework.viewsets import ModelViewSet
from .models import asisten
from .serializer import asistenSerializer

# Create your views here.

class AsistenViewSet (ModelViewSet):
    serializer_class = asistenSerializer
    queryset = asisten.objects.all()