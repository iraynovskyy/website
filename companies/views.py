from django.shortcuts import render

from django.shortcuts import get_object_or_404
from rest_framework.views import APIView          # make these normal views return API data
from rest_framework.response import Response      # we can send a specific response status
from rest_framework import status
from .models import Stock
from.serializers import StockSerializer

# Create your views here.

# List all stocks or create a new one
# stocks/FB/ or /AMZN/
class StockList(APIView):

    def get(self, request):     # reading information
        stocks = Stock.objects.all()
        serializer = StockSerializer(stocks, many=True)
        return Response(serializer.data)

    def post(self):    # submitting the form
        pass

from django.views import generic
from music.models import Album

class HomeView(generic.ListView):
    template_name = 'music/home.html'
    context_objext_name = 'all_albums'

    def get_queryset(self):
        return Album.objects.all()