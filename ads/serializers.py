from rest_framework import serializers

from .models import Ad , PriceEstimate

class AdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ad
        fields = "__all__"
