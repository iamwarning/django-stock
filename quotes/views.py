from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'hello.html', {})


def about(request):
    return render(request, 'about.html', {})
