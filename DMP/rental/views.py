from django.shortcuts import render, get_object_or_404
from .models import Rental
# Create your views here.


def rental(request):
    rental = Rental.objects.all()
    pa_ti = "On Rent"
    context = {
        'rental': rental,
        'tit': pa_ti
    }
    return render(request, 'ready/ongoing.html', context=context)

# Check ID values


def listing_rent(request, rental_id):
    rental = get_object_or_404(Rental, pk=rental_id)
    pa_ti = "On Rent"
    context = {
        'rental': rental,
        'tit': pa_ti
    }
    return render(request, 'ongoing/individual.html', context=context)


def search(request):
    return render(request, 'ready/search.html')
