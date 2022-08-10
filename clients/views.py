from django.shortcuts import render

# Create your views here.

def base(request):
    return render (request,'clients/partials/base.html')


def home(request):
    return render (request,'clients/index.html')    



def updation(request):
    return render (request,'clients/updation.html')




def payment(request):
    return render (request,'clients/payment.html')    