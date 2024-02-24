from django.urls import path

from microservice.views import ItemsView, ItemDetailView

urlpatterns = [
    path('get_items/', ItemsView.as_view(), name='gett'),
    path('delete_items/', ItemsView.as_view(), name='delette'),
    path('create_item/', ItemsView.as_view(), name='postt'),
    path('get_item/<int:item_id>/',  ItemDetailView.as_view(), name='get'),
    path('change_item/<int:item_id>/', ItemDetailView.as_view(), name='put'),
    path('delete_item/<int:item_id>/', ItemDetailView.as_view(), name='delete'),
]
