from rest_framework import serializers
from .models import Node

class NodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Node
        fields = '__all__'
        read_only_fields = ('id', 'created_at', 'updated_at')
