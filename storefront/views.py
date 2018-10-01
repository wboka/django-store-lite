from django.shortcuts import render

from .forms import OrderForm

def store(request):
    """ Online Store. Currently an order form. """
    if request.method == 'POST':
        form = OrderForm(request.POST)
    else:
        form = OrderForm()

    return render(request, 'storefront/order-form.html', {'form': form})
