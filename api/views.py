from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Node
from .serializers import NodeSerializer


class TreeView(APIView):

    def get(self, request):
        try:
            """
            Get all nodes
            """
            parent_id = request.query_params.get('parent_id')
            full = request.query_params.get('all') == 'true'

            if parent_id:
                # Get children for specific node
                nodes = Node.objects.filter(parent=parent_id)
            else:
                # Get all root nodes
                nodes = Node.objects.filter(parent__isnull=True)
            
            serializer = NodeSerializer(nodes, many=True, context={'full': full})
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
            Create a new node
            """
            node_data = request.data
            serializer = NodeSerializer(data=node_data, partial=True)

            if not serializer.is_valid():
                return Response({
                    'status': 'error',
                    'message': 'Invalid data',
                    'errors': serializer.errors
                }, status=status.HTTP_400_BAD_REQUEST)

            serializer.save()

            return Response({
                'status': 'success',
                'message': 'Node created successfully',
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
            Update a node
            """
            node_id = request.query_params.get('id')

            if not node_id:
                return Response({
                    'status': 'error',
                    'message': 'Node ID is required'
                }, status=status.HTTP_400_BAD_REQUEST)
            
            node = Node.objects.get(id=node_id)
            if not node:
                return Response({
                    'status': 'error',
                    'message': 'Node not found'
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
                'message': 'Node updated successfully',
                'data': serializer.data
            }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({
                'status': 'error',
                'message': 'An error occurred',
                'error': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

    def delete(self, request):
        try:
            """
            Delete a node
            """
            node_id = request.query_params.get('id')

            if not node_id:
                return Response({
                    'status': 'error',
                    'message': 'Node ID is required'
                }, status=status.HTTP_400_BAD_REQUEST)
            
            node = Node.objects.get(id=node_id)
            if not node:
                return Response({
                    'status': 'error',
                    'message': 'Node not found'
                }, status=status.HTTP_404_NOT_FOUND)
            
            node.delete()

            return Response({
                'status': 'success',
                'message': 'Node deleted successfully'
            }, status=status.HTTP_200_OK)

        except Exception as e:
            return Response({
                'status': 'error',
                'message': 'An error occurred',
                'error': str(e)
            }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

