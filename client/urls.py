from django.urls import path
from . import views

app_name = 'client'

urlpatterns = [
    path('nouveau_client/', views.new_client, name='new_client'),
    path('modifier_client/<str:id>/', views.modify_client, name='modify_client'),
    path('supprimer_client/<str:id>/', views.delete_client, name='delete_client'),
    path('supprimer_commande_client/<str:id>/', views.delete_client_command, name='delete_client_command'),
    path('mettre_a_jour_commande_client/<str:id>/', views.update_client_command, name='update_client_command'),
    path('<str:id>/', views.list_client, name='list_client'),
]
