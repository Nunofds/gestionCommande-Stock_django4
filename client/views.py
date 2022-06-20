from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from client.models import Client
from command.filters import CommandFilter


@login_required(login_url='account:connexion')
def list_client(request, id=None):
    client = Client.objects.get(id=id)   # recup le client via le id
    commande = client.command_set.all()  # recup toutes les commandes du client (via l'id precedent)
    total_commandes = commande.count()      # recup le nombre total de commandes du client (via la ligne precedente)

    # Création du filtre
    my_filter = CommandFilter(request.GET, queryset=commande)
    commande = my_filter.qs    # mets à jour les commandes en fonction du filtre

    context = {'client_id': client,
               'commande_client': commande,
               'total_commandes': total_commandes,
               'myFilter': my_filter}
    return render(request, 'client/index.html', context)

