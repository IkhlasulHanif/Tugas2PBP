from django.shortcuts import render

from mywatchlist.models import MyWatchlistItem
from django.http import HttpResponse
from django.core import serializers

def show_mywatchlist(request):
    item_list_watchlist = MyWatchlistItem.objects.all()
    context = {
    'item_list': item_list_watchlist,
    'nama': 'Ikhlasul Akmal Hanif',
    'npm' : '2106650462',
    }
    return render(request, "mywatchlist.html", context)

def show_xml(request):
    data = MyWatchlistItem.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = MyWatchlistItem.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


