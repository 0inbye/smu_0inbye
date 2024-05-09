from django.shortcuts import render

# Create your views here.

def success(request):
    return render(request,'api_app/success.html')
    