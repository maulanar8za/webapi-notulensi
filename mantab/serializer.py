
from rest_framework.serializers import ModelSerializer
from .models import asisten

class asistenSerializer (ModelSerializer):
    class Meta:
        model = asisten
        fields = '__all__'