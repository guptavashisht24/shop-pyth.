from django.shortcuts import render
from django.http import HttpResponse
from django.core.cache import cache
from .models import Description, Bill, Customer, Sale
from .forms import DForm, BForm, SForm, CForm

# Create your views here.
def index(request):
    context = {}
    return render(request, 'front/index.html', context)

def sale(request):
    context = {}
    return render(request, 'front/sale.html', context)

def commitcust(request):
    if request.method == "POST":
        form = CForm(request.POST)
        if form.is_valid():
            customer = form.save()
            return HttpResponse(str(customer.phone))
        print form.errors
        return HttpResponse("Fail")
    return HttpResponse("only POST is possible")

def commitsale(request):
    if request.method == "POST":
        form = SForm(request.POST)
        if form.is_valid():
            sale = form.save(commit=False)
            new_id = cache.get('today')+str(cache.get('sale'))
            cache.set('sale',int(str(cache.get('sale')))+1, None)
            sale.id = new_id
            sale.save()
            return HttpResponse(new_id)
        print form.errors
        return HttpResponse("Fail Form")
    return HttpResponse("only POST is possible")

def item(request, itemID):
    if request.method == "GET":

        try:
            desc = Description.objects.get(pk=itemID)
            dd = {"desc":str(desc.desc), "quality":str(desc.quality), "rate":str(desc.rate)}
            return HttpResponse(str(dd))
        except:
            return HttpResponse("Fail")

    return HttpResponse("only GET is possible")

def cust_phone(request, phone):
    if request.method == "GET":

        try:
            cust = Customer.objects.get(pk=phone)
            dd = {"name":str(cust.name), "email":str(cust.email)}
            return HttpResponse(str(dd))
        except:
            return HttpResponse("Fail")

    return HttpResponse("only GET is possible")

def commitvalues(request):
    if request.method == "POST":
        form = DForm(request.POST)
        if form.is_valid():
            description = form.save(commit=False)
            new_id = cache.get('today')+str(cache.get('description'))
            cache.set('description',int(str(cache.get('description')))+1, None)
            description.id = new_id
            description.save()
            return HttpResponse(new_id)
        print form.errors
        return HttpResponse("Fail")
    return HttpResponse("only POST is possible")

def commitbill(request):
    if request.method == "POST":
        form = BForm(request.POST, request.FILES)
        if form.is_valid():
            new_id = cache.get('today')+str(cache.get('bill'))
            handle_uploaded_image(new_id, request.FILES['bill_image'])
            bill = form.save(commit=False)
            cache.set('bill',int(str(cache.get('bill')))+1, None)
            bill.id = new_id
            bill.save()
            return HttpResponse(new_id)
        print form.errors
        return HttpResponse("fail")
    return HttpResponse("only POST is possible")

def handle_uploaded_image(iid,f):
    with open('front/media/'+iid+f.__str__(), 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    destination.close()
