from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from client.models import Client
from command.filters import CommandFilter
from command.forms import CommandForm
from command.models import Command
from .forms import NewClientForm


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


@login_required(login_url='account:connexion')
def new_client(request):
    form = NewClientForm()
    if request.method == 'POST':
        form = NewClientForm(request.POST)
        if form.is_valid():
            form.save()
            client = form.cleaned_data.get('name')
            messages.success(request, 'Compte crée avec succèss pour "' + client + '"')
            return redirect('product:home')

    context = {'form': form}
    return render(request, 'client/new_client.html', context)


@login_required(login_url='account:connexion')
def modify_client(request, id=None):
    client = Client.objects.get(id=id)
    form = NewClientForm(instance=client)
    if request.method == 'POST':
        form = NewClientForm(request.POST, instance=client)
        if form.is_valid():
            form.save()
            return redirect('product:home')

    context = {'form': form}
    return render(request, 'client/new_client.html', context)


@login_required(login_url='account:connexion')
def delete_client(request, id=None):
    client = Client.objects.get(id=id)
    if request.method == 'POST':
        client.delete()
        return redirect('product:home')

    context = {'client': client}
    return render(request, 'client/delete_client.html', context)


@login_required(login_url='account:connexion')
def update_client_command(request, id=None):
    command_client = Command.objects.get(id=id)
    form = CommandForm(instance=command_client)
    if request.method == 'POST':
        form = CommandForm(request.POST, instance=command_client)
        if form.is_valid():
            form.save()
            return redirect('product:home')

    context = {'form': form}
    return render(request, 'command/add_command.html', context)


@login_required(login_url='account:connexion')
def delete_client_command(request, id=None):
    command_client = Command.objects.get(id=id)
    if request.method == 'POST':
        command_client.delete()
        return redirect('product:home')
    context = {'item_delete': command_client}
    return render(request, 'command/delete_command.html', context)
