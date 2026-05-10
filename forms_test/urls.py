from django.urls import path
from .views import (
    register_view,
    UserProfileView
)

urlpatterns = [

    path(
        'register/',
        register_view,
        name='register'
    ),
    path(
        'profile/',
        UserProfileView.as_view(),
        name='profile'
    ),
]
