from django.shortcuts import render
from django.http import HttpResponse
from .forms import AddItemForm
from .models import InventoryItem
from kibat.settings import BASE_DIR
from django.conf import settings
import os
from django.http import HttpResponse, Http404


def IndexView(request):
    return render(request, 'inventory/index.html')


def add_itemform(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        val_1 = request.POST['property_name']
        val_2 = request.POST['category_name']
        val_3 = request.POST['unit_id']
        val_4 = request.POST['costing']
        val_5 = request.POST['price']
        val_6 = request.POST['is_inactive']

        ins = InventoryItem(property_name=val_1, category_name=val_2, unit_id=val_3,
                            costing=val_4, price=val_5, is_inactive=val_6)
        ins.save()

        # redirect to a new URL:
        return HttpResponse('thanks')

    # if a GET (or any other method) create a blank form
    else:
        form = AddItemForm()

    return render(request, 'inventory/add.html', {'form': form})


def import_structure_download(request):
    file_path = os.path.join(settings.MEDIA_ROOT, 'import_structure.xlsx')
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
            response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)
            return response


def all_units(request):
    units = InventoryItem.objects.all()
    return render(request, 'inventory/unit_master.html', {'unit_master': units})
