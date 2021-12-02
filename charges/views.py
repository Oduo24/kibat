from django.shortcuts import render
from .models import Charges


def ChargeSheet(request):
    charges_info = Charges.objects.all()
    return render(request, 'charges/charge_sheet.html', {'charge_sheet': charges_info})
