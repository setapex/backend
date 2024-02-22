from django.urls import path
from .views import CustomObtainAuthToken, CreateUserView

urlpatterns = [
    path('login/', CustomObtainAuthToken.as_view(), name='token_obtain_pair'),
    path('create/', CreateUserView.as_view(), name='create_user'),
]
