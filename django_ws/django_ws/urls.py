from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)
from websocket.views import MessageSendAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('message/', MessageSendAPIView.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
