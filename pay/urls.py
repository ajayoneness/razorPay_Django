from django.urls import path
from .views import rezPay,Pay


urlpatterns = [
    path('',rezPay,name="pay"),
    path('pay/',Pay,name="rezpay"),
]
