from django.urls import path
from . import views

app_name = 'command'

urlpatterns = [
    path('liste_commandes/', views.list_command, name='list_command'),
    path('ajout_commande/', views.add_command, name='add_command'),
    path('modifier_commande/<str:id>', views.modify_command, name='modify_command'),
    path('supprimer_commande/<str:id>', views.delete_command, name='delete_command'),
]

