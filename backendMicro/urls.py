
from django.contrib import admin
from django.urls import path, include

from back.views import UserProfileView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('back.urls')),
    path('', include('microservice.urls')),
    path('profiles/<int:user_id>/', UserProfileView.as_view(), name='other_user_profile'),
]
