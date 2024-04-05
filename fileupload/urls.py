
from django.urls import path
from .views import *
urlpatterns = [
 path('files',FileApiView.as_view(),name="list-create"),   
 path('files/<int:pk>/',FileApiView.as_view(),name="update-get-create")   
]
