from django.shortcuts import render, redirect
from .forms import CoinForm
from .models import Coin
from django.contrib import messages

def add_coin(request):
    if request.method == 'POST':
        form = CoinForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_coins')
    else:
        form = CoinForm()
    return render(request, 'coin/add_coin.html', {'form': form})


def list_coins(request):
    coins = Coin.objects.all() # retrieve all the recipes
    return render(request, 'coin/list_coins.html', {'coins': coins})


def update_coin(request, coin_id):
    coin = Coin.objects.get(pk=coin_id)
    if request.method == 'POST':
        form = CoinForm(request.POST, instance=coin)
        if form.is_valid():
            form.save()
            return redirect('list_coins')
    else:
        form = CoinForm(instance=coin)
    return render(request, 'coin/update_coin.html', {'form': form})

def delete_coin(request, coin_id):
    recipe = Coin.objects.get(pk=coin_id)
    recipe.delete()
    messages.success(request, 'Coin deleted successfully.')
    return redirect('list_coins')


def search_coins(request):
    query = request.GET.get('q')
    coins = Coin.objects.filter(name__icontains=query)
    print(coins, 'display coins')
    return render(request, 'coin/search_coin.html', {'coins': coins, 'query': query})





