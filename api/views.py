from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Node
from .serializers import NodeSerializer


class TreeView(APIView):

    def get(self, request):
        try:
            """
            Get all root nodes (trees)
            """
            parents = Node.objects.filter(parent__isnull=True)
            serializer = NodeSerializer(parents, many=True)
            return Response({
                'status': 'success',
                'message': 'Trees fetched successfully',
                'data': serializer.data
            }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({
                'status': 'error',
                'message': 'An error occurred',
                'error': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def post(self, request):
        try:
            """
            Create a new tree (root node)
            """
            tree_data = request.data
            serializer = NodeSerializer(data=tree_data, partial=True)

            if not serializer.is_valid():
                return Response({
                    'status': 'error',
                    'message': 'Invalid data',
                    'errors': serializer.errors
                }, status=status.HTTP_400_BAD_REQUEST)

            serializer.save()

            return Response({
                'status': 'success',
                'message': 'Tree created successfully',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)

        except Exception as e:
            return Response({
                'status': 'error',
                'message': 'An error occurred',
                'error': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    def put(self, request):
        try:
            """
            Update a tree (root node)
            """
            tree_id = request.query_params.get('id')

            if not tree_id:
                return Response({
                    'status': 'error',
                    'message': 'Tree ID is required'
                }, status=status.HTTP_400_BAD_REQUEST)
            
            node = Node.objects.get(id=tree_id, parent=None)
            if not node:
                return Response({
                    'status': 'error',
                    'message': 'Tree not found'
                }, status=status.HTTP_404_NOT_FOUND)
            
            serializer = NodeSerializer(node, data=request.data, partial=True)

            if not serializer.is_valid():
                return Response({
                    'status': 'error',
                    'message': 'Invalid data',
                    'errors': serializer.errors
                }, status=status.HTTP_400_BAD_REQUEST)

            serializer.save()

            return Response({
                'status': 'success',
                'message': 'Tree updated successfully',
                'data': serializer.data
            }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({
                'status': 'error',
                'message': 'An error occurred',
                'error': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
