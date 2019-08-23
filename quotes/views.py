from django.shortcuts import render, redirect
from quotes.models import Stock
from django.contrib import messages
from .forms import StockForm


def home(request):
    # pk_18020125b9404116be195d47eee8f33e
    import requests
    import json

    if request.method == 'POST':
        ticker = request.POST['ticker']
        api_request = requests.get(
            "https://cloud.iexapis.com/stable/stock/" + ticker + "/quote/?token=pk_18020125b9404116be195d47eee8f33e")
        # noinspection PyBroadException
        try:
            api = json.loads(api_request.content)
        except Exception as ex:
            api = "Error..."
        return render(request, 'hello.html', {'api': api})
    else:
        return render(request, 'hello.html', {'ticker': "Enter a Ticker Symbol Above..."})


def about(request):
    return render(request, 'about.html', {})


def add_stock(request):
    if request.method == 'POST':
        form = StockForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Stock Has Been Added!')
            return redirect('add_stock')
    else:
        ticker = Stock.objects.all()
        return render(request, 'addStock.html', {'ticker': ticker})


def delete_stock(request, id_stock):
    item = Stock.objects.get(pk=id_stock)
    item.delete()
    messages.success(request, 'Stock Has Been Deleted!')
    return redirect(add_stock)