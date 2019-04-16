from django.shortcuts import get_object_or_404, render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.base import ContextMixin
from .models import Listing
from news.models import Review


class Allls_cbv(ListView):
    template_name = "listings/listings_cbv.html"
    queryset = Listing.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['number'] = random.randrange(1, 100)
        context['title'] = "All Of Our Amazing Properties"
        context['sub'] = "We are excited to have you here"
        return context


class Ong_cbv(ListView):
    template_name = "listings/listings_cbv.html"
    queryset = Listing.objects.filter(category='Ongoing')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['number'] = random.randrange(1, 100)
        context['title'] = "Upcoming Properties Listed Here"
        context['sub'] = "Pre-book your dream home"
        return context


class Ongoing_cbv(DetailView):
    template_name = "listings/listing.html"
    queryset = Listing.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reviews'] = Review.objects.filter(
            project__name=self.object.name)
        return context


class Buyls_cbv(ListView):
    template_name = "listings/listings_cbv.html"
    queryset = Listing.objects.filter(category='Buy')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Properties Which You Can Own"
        context['sub'] = "Don't fall behind! Now is the Time."
        return context


class Rentls_cbv(ListView):
    template_name = "listings/listings_cbv.html"
    queryset = Listing.objects.filter(category='Rent')

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Fantastic Living Spaces On Rent"
        context['sub'] = "Here are opportunities not to miss!"
        return context


class Searchls_cbv(ListView):
    template_name = "listings/listings_cbv.html"
    #queryset = Listing.objects.filter(category='Rent')

    def get_queryset(self, *args, **kwargs):
        request = self.request
        print(request.GET)
        query = request.GET.get('Keyword')
        if query is not None:
            return Listing.objects.filter(name__icontains=query)
        return Listing.objects.none()

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = "Your Search Results"
        context['sub'] = "Search with the name of the Property you are looking for"
        return context
