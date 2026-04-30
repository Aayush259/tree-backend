from rest_framework import serializers
from .models import Node

class NodeSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()

    class Meta:
        model = Node
        fields = ['id', 'name', 'data', 'parent', 'children', 'created_at', 'updated_at']
        read_only_fields = ('id', 'created_at', 'updated_at')

    def get_children(self, obj):
        # Only recurse if the context 'full' is True
        if self.context.get('full'):
            serializer = NodeSerializer(obj.children.all(), many=True, context=self.context)
            return serializer.data
        # Otherwise return just the IDs
        return [child.id for child in obj.children.all()]
