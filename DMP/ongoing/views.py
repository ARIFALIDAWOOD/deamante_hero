from django.shortcuts import get_object_or_404, render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.base import ContextMixin
# Create your views here.
from .models import Ongoing
from news.models import ReviewsOngoing


def ongoing(request):
    ongo = Ongoing.objects.all()
    context = {
        'ongoing': ongo
    }
    return render(request, 'ongoing/ongoing.html', context=context)

# Check ID values


def listing(request, ongoing_id):
    listing = get_object_or_404(Ongoing, pk=ongoing_id)
    reviews = ReviewsOngoing.objects.all()
    pa_ti = "ongoing"
    context = {
        'listing': listing,
        'tit': pa_ti,
        'reviews': reviews
    }
    return render(request, 'ongoing/individual.html', context=context)


def search(request):
    return render(request, 'ongoing/search.html')


class Ong_cbv(ListView):
    template_name = "ongoing/ongoing_cbv.html"
    queryset = Ongoing.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        #context['number'] = random.randrange(1, 100)
        print(context)
        return context


class Ongoing_cbv(DetailView):
    template_name = "ongoing/individual_cbv.html"
    queryset = Ongoing.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = ReviewsOngoing.objects.filter(
            name=Ongoing._meta.pk.name)
        print(context)
        return context
