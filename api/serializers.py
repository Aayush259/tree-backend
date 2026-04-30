from rest_framework import serializers
from .models import Node

class NodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Node
        fields = ['id', 'name', 'data', 'parent', 'children', 'created_at', 'updated_at']
        read_only_fields = ('id', 'created_at', 'updated_at')
