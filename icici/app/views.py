from django.shortcuts import render, redirect
from .forms import CustomerForm
from .models import Customer

def customer_details(request):
    if request.method == 'POST':
        form = CustomerForm(request.POST)
        if form.is_valid():
            customer = form.save()
            return render(request, 'app/success.html', {'customer_id': customer.customer_id})
    else:
        form = CustomerForm()
    return render(request, 'app/customer_form.html', {'form': form})

def success(request):
    return render(request, 'app/success.html')
