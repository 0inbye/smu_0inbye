from django.urls import path
from kakaopay import views

app_name = 'kakaopay'

urlpatterns = [
    path('', views.kakaopay, name='kakaopay'),
    path('index/', views.index, name='index'),
    path('paySuccess/', views.paySuccess, name='paySuccess'),
    path('payFail/', views.payFail),
    path('payCancel/', views.payCancel),
]