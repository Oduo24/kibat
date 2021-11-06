from django.shortcuts import render, HttpResponse
from .models import CompanyInfo
from .forms import CompanyInfoForm


# Create your views here.


def CompanyInfoView(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        val_1 = request.POST['company_name']
        val_2 = request.POST['city']
        val_3 = request.POST['email']
        val_4 = request.POST['phone_number']
        val_5 = request.POST['company_logo']

        ins = CompanyInfo(company_name=val_1, city=val_2, email=val_3,
                          phone_number=val_4, company_logo=val_5)
        ins.save()

        # redirect to a new URL:
        return HttpResponse('thanks')

    # if a GET (or any other method) create a blank form
    else:
        form = CompanyInfoForm()

    return render(request, 'configuration/company_info.html', {'form': form})
