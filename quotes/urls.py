from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about.html', views.about, name="about"),
    path('addStock.html', views.add_stock, name="add_stock"),
    path('delete/<id_stock>', views.delete_stock, name="delete"),
]
