from django.shortcuts import render, get_object_or_404
from .models import Employee, Carousel
from ongoing.models import Ongoing
from rental.models import Rental
from buy.models import Buy
from news.models import News
# Create your views here.


def index(request):
    caro = Carousel.objects.all()
    news = News.objects.all()
    context = {
        'carousel': caro,
        'news': news
    }
    return render(request, 'pages/index.html', context=context)


def all(request):
    ongo = Ongoing.objects.all()
    buy = Buy.objects.all()
    rent = Rental.objects.all()
    context = {
        'ongoing': ongo,
        'buy': buy,
        'rent': rent}
    return render(request, 'pages/all.html', context)

# def ongoing(request):
    # return render(request, 'pages/ongoing.html')


def about(request):
    emp = Employee.objects.all()
    context = {
        'employee': emp
    }
    return render(request, 'pages/about.html', context=context)


def contact(request):
    return render(request, 'pages/contact.html')


def coming(request):
    return render(request, 'ComingSoon/index.html')
