from django.shortcuts import render
from command.models import Command
from client.models import Client
from django.contrib.auth.decorators import login_required


@login_required(login_url='account:connexion')
def home(request):
    commands = Command.objects.all()
    clients = Client.objects.all()

    context = {'commands': commands, 'clients': clients}

    return render(request, 'product/index.html', context)
