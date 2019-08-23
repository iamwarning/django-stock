from django.shortcuts import render


# Create your views here.
def home(request):
    # pk_18020125b9404116be195d47eee8f33e
    import requests
    import json

    api_request = requests.get("https://cloud.iexapis.com/stable/stock/aapl/quote/latestPrice?token=pk_18020125b9404116be195d47eee8f33e")
    # noinspection PyBroadException
    try:
        api = json.loads(api_request.content)
    except Exception as ex:
        api = "Error..."

    return render(request, 'hello.html', {'api': api})


def about(request):
    return render(request, 'about.html', {})
