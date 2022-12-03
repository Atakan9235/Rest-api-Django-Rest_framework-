from rest_framework import serializers
from .models import Kimlik

class  KimlikSerializer(serializers.ModelSerializer) :
    class Meta:
        model=Kimlik
        fields=('id','Ad','Soyad')