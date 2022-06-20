from django.urls import path
from . import views

app_name = 'client'

urlpatterns = [
    path('<str:id>/', views.list_client, name='list_client')
]
