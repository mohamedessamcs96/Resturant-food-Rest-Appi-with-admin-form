from django.db.models import fields
from rest_framework import serializers



from .models import Menu

class FoodSerializers(serializers.ModelSerializer):
    class Meta:
        model=Menu
        fields='__all__'