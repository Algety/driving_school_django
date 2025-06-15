from django.urls import path
from .views import ContentBlockList, TeamBlockList

urlpatterns = [
    path('', ContentBlockList.as_view(), name='home'),
    path('team/', TeamBlockList.as_view(), name='team'),
]
