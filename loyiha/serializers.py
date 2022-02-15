from rest_framework import serializers
from .models import *

class LoyihaSerializer(serializers.ModelSerializer):
    
    class Meta():
        model = Loyiha
        fields = '__all__'

class IshchiSerializer(serializers.ModelSerializer):

    class Meta():
        model = Ishchi
        fields = '__all__'

class KategoriyaSerializer(serializers.ModelSerializer):
    kategoriya = LoyihaSerializer(read_only=True, many=True)
    class Meta():
        model = Kategoriya
        fields = '__all__'