from rest_framework import serializers
from .models import Itemstock

class StockSerializer(serializers.ModelSerializer):
    
    # description = serializers.SlugRelatedField(queryset=Stock.objects.all(), slug_field='name')
    # description_display = serializers.CharField(source='description', read_only=True)

    class Meta:
        model = Itemstock
        fields = "__all__"
