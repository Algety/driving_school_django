from django.urls import path
from .views import ContentBlockList

urlpatterns = [
    path('', ContentBlockList.as_view(), name='home'),
]
