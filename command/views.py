from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from command.forms import CommandForm
from .models import Command


@login_required(login_url='account:connexion')
def list_command(request):
    commands = Command.objects.all()
    context = {'commands': commands}
    return render(request, 'command/list_command.html', context)


@login_required(login_url='account:connexion')
def add_command(request):
    form = CommandForm()
    if request.method == 'POST':
        form = CommandForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'command/add_command.html', context)


@login_required(login_url='account:connexion')
def modify_command(request, id):
    commande = Command.objects.get(id=id)
    form = CommandForm(instance=commande)
    if request.method == 'POST':
        form = CommandForm(request.POST, instance=commande)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'command/add_command.html', context)


@login_required(login_url='account:connexion')
def delete_command(request, id):
    command = Command.objects.get(id=id)
    if request.method == 'POST':
        command.delete()
        return redirect('/')
    context = {'item': command}
    return render(request, 'command/delete_command.html', context)

