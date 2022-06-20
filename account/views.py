from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import UserCreation


def inscriptionPage(request):
    form = UserCreation()
    if request.method == 'POST':
        form = UserCreation(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, 'Compte crée avec succèss pour ' + user)
            return redirect('account:connexion')

    context = {'form': form}
    return render(request, 'account/inscription.html', context)


def accessPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('product:home')
        else:
            messages.info(request, 'Erreur: nom d\'utilisateur et/ou mot de passe incorrects.')

    context = {}
    return render(request, 'account/access.html', context)


def logoutUser(request):
    logout(request)
    return redirect('account:connexion')
