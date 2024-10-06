from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

tax_rate = 0.15

def index(request):
    return HttpResponse("<h1>this is a site to calculate tax.</h1>")

def cal_tax(requesst, number):
    try:
       number = float(number)
       price = number + (number*tax_rate)
       return HttpResponse(f"<h1>the total price after the tax {price}</h1>")
    except ValueError:
        return HttpResponse("invalid input")
def taxview(request):
    tax = tax_rate * 100
    return HttpResponse(f"<h1>tax rate: {tax}% </h1>")
