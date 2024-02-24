from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .microservice_client import MicroserviceClient


class ItemsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user_token = request.headers.get('Authorization').split()[1]
        microservice_client = MicroserviceClient('http://localhost:8000')
        items = microservice_client.get_items(user_token)
        return Response(items, status=status.HTTP_200_OK)

    def delete(self, request):
        user_token = request.headers.get('Authorization').split()[1]
        microservice_client = MicroserviceClient('http://localhost:8000')
        result =  microservice_client.delete_all_items(user_token)
        return Response(result, status=status.HTTP_204_NO_CONTENT)

    def post(self, request):
        user_token = request.headers.get('Authorization').split()[1]
        item_data = request.data
        microservice_client = MicroserviceClient('http://localhost:8000')
        created_item =  microservice_client.create_item(user_token,item_data)
        return Response(created_item, status=status.HTTP_201_CREATED)


class ItemDetailView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, item_id):
        user_token = request.headers.get('Authorization').split()[1]
        microservice_client = MicroserviceClient('http://localhost:8000')
        item = microservice_client.get_item_by_id(user_token, item_id)
        return Response(item, status=status.HTTP_200_OK)

    def put(self, request, item_id):
        user_token = request.headers.get('Authorization').split()[1]
        item_data = request.data
        microservice_client = MicroserviceClient('http://localhost:8000')
        updated_item = microservice_client.update_item(user_token,item_id, item_data)
        return Response(updated_item, status=status.HTTP_200_OK)

    def delete(self, request, item_id):
        user_token = request.headers.get('Authorization').split()[1]
        microservice_client = MicroserviceClient('http://localhost:8000')
        deleted_item = microservice_client.delete_item(user_token,item_id)
        return Response(deleted_item, status=status.HTTP_204_NO_CONTENT)
