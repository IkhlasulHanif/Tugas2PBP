from django.shortcuts import render
from katalog.models import CatalogItem

# Create your views here.
def show_katalog(request):
    item_list_catalog = CatalogItem.objects.all()
    context = {
    'item_list': item_list_catalog,
    'nama': 'Hanif'
    }
    return render(request, "katalog.html", context)