from django.shortcuts import render
from django.http import HttpResponse
from .models import Description, Bill
from django.http import Http404
from .forms import DForm
from .forms import BForm
import pprint
# Create your views here.
def index(request):
    context = {}
    return render(request, 'front/index.html', context)


def bill(request):
    try:
        billinfo = Description.objects.all()
        context = {'billinfo': billinfo}
    except Description.DoesNotExist:
        raise Http404("No Bills")
    return render(request, 'front/bill.html', context)

def commitvalues(request):
    if request.method == "POST":
        form = DForm(request.POST)
        if form.is_valid():
            Description = form.save()
            print Description
            return HttpResponse("Hello;You're at the front index.Commit's done!")
        print form.errors
        return HttpResponse("Fail")

def commitbill(request):
    if request.method == "POST":
        form = BForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_image(request.FILES['bill_image'])
            print form
            Bill = form.save()
            return HttpResponse(str(Bill.bill_id()))
        print form.errors
        return HttpResponse("fail")

def handle_uploaded_image(f):
    with open('front/media/'+f.__str__(), 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    destination.close()
