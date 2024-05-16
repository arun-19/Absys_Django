from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def PurChage_Master(request):
    return render(request, "purchaseM.html",context={
        'title':"Purchase"
    })