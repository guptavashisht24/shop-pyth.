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
            return HttpResponse("Hello;You're at the front index.Commit's done!")
        print form.errors
        return HttpResponse("Fail")

def commitbill(request):
    if request.method == "POST":
        form = BForm(request.POST)
        if form.is_valid():
            Bill = form.save()
            return HttpResponse("Hello;You're at the front index.Commit's done!")
        print form.errors
        return HttpResponse("Fail")
