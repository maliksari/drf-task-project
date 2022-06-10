from django.urls import path

from .views import register, token, refresh_token, revoke_token

urlpatterns = [
    path('register/', register, name='register'),
    path('token/', token, name="token"),
    path('token/refresh/', refresh_token, name="refresh"),
    path('token/revoke/', revoke_token, name="revoke"),
]
