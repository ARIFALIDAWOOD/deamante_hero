from django.shortcuts import render, get_object_or_404
from .models import Buy

# Create your views here.


def buy(request):
    buy_e = Buy.objects.all()
    pa_ti = "On Sale"
    context = {
        'buy': buy_e,
        'tit': pa_ti

    }
    return render(request, 'ready/ongoing.html', context=context)

# Check ID values


def listing_buy(request, buy_id):
    buy = get_object_or_404(Buy, pk=buy_id)
    pa_ti = "On Sale"
    context = {
        'buy': buy,
        'tit': pa_ti
    }
    return render(request, 'ongoing/individual.html', context=context)


def search(request):
    return render(request, 'ready/search.html')
