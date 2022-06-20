from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('inscription/', views.inscriptionPage, name='inscription'),
    path('connexion/', views.accessPage, name='connexion'),
    path('deconnexion/', views.logoutUser, name='logout'),
]
