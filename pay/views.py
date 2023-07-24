from django.shortcuts import render
import razorpay
from razorPay.settings import RAZORPAY_KEY_ID,RAZORPAY_KEY_SECRET


def rezPay(request):
    return render(request,'pay.html')



def Pay(request):
    client = razorpay.Client(auth=(RAZORPAY_KEY_ID, RAZORPAY_KEY_SECRET))

    data = {"amount": 500, "currency": "INR", "receipt": "codeaj"}
    payment = client.order.create(data=data)
    print(payment)

    return render(request,'pay.html',payment)