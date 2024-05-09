# api_app/views.py
from django.shortcuts import render

def success(request):
    full_address = request.GET.get('fullAddress')  # GET 매개변수에서 fullAddress 값을 가져옴
    return render(request, 'api_app/success.html', {'full_address': full_address})
