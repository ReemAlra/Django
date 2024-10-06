from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:number>/", views.cal_tax, name="calculate_tax"),
    path("taxrate/", views.taxview, name="tax_rate"),
]