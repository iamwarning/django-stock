from django.shortcuts import render


# Create your views here.
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
