from django.shortcuts import render

from mywatchlist.models import MyWatchlistItem
from django.http import HttpResponse
from django.core import serializers

def show_mywatchlist(request):
    item_list_watchlist = MyWatchlistItem.objects.all()
    watched_cnt = 0
    for item in item_list_watchlist:
        if item.watched:
            watched_cnt += 1
    if (watched_cnt*2 >= len(item_list_watchlist)):
        is_watched_cnt = True
    else:
        is_watched_cnt = False
    context = {
    'item_list': item_list_watchlist,
    'nama': 'Ikhlasul Akmal Hanif',
    'npm' : '2106650462',
    'is_watched_cnt' : is_watched_cnt
    }
    return render(request, "mywatchlist.html", context)

def show_xml(request):
    data = MyWatchlistItem.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = MyWatchlistItem.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")


