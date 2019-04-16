from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from .models import Employee, Carousel, About
from listings.models import Listing
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


def about(request):
    emp = Employee.objects.all()
    abt = About.objects.filter(name='use')
    context = {
        'employee': emp,
        'about': abt
    }
    return render(request, 'pages/about.html', context=context)


def contact(request):
    return render(request, 'pages/contact.html')


def coming(request):
    return render(request, 'ComingSoon/index.html')


class Search_ls(ListView):
    template_name = "ready/search.html"
    #queryset = Ongoing.objects.all()

    def get_queryset(self, *args, **kwargs):
        #context = super().get_context_data(**kwargs)
        # context['number'] = random.randrange(1, 100)
        request = self.request
        return


class Search(DetailView):
    template_name = "ongoing/individual_cbv.html"
    #queryset = Ongoing.objects.all()
    # temp = Ongoing
    # print(queryset)

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['reviews'] = ReviewsOngoing.objects.filter(
        #   project__name=self.object.name)
        #listing = get_object_or_404(Ongoing, pk=kwargs)
        # print(self.object.name)
        return context
