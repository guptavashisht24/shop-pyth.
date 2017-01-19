from django.shortcuts import render
from django.http import HttpResponse
from django.core.cache import cache
from .models import Description, Bill, Customer, Sale
from .forms import DForm, BForm, SForm, CForm
from shop.settings import MEDIA_URL
import qrcode
# Create your views here.
def home(request):
    #Link for Landing Page
    context = {}
    return render(request,'front/home.html',context)
def index(request):
    context = {}
    return render(request, 'front/index.html', context)

def sale(request):
    context = {}
    return render(request, 'front/sale.html', context)

def custbill(request):
    if request.method == "GET":

        try:
            phone = request.GET['phone_num']
            cust = Sale.objects.filter(cust_id=phone)
            context = {'cust': cust}
            
        except Customer.DoesNotExist:
              raise Http404("No Sale for the customer exists")
    return render(request, 'front/orders.html', context)

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
            idr = form.cleaned_data['item_id']
            lengthr = form.cleaned_data['length']
            custidr = form.cleaned_data['cust_id']
            qrdata = str(idr)+"\n"+str(lengthr)+"\n"+str(custidr)+"\n"
            img = qrcode.make(qrdata)
            
            sale = form.save(commit=False)
            new_id = cache.get('today')+str(cache.get('sale'))
            var = "front/templates/front/Billimg/"+str(new_id)+".png"
            img.save(var,'PNG')
            cache.set('sale',int(str(cache.get('sale')))+1, None)
            sale.id = new_id
            sale.save()
            return HttpResponse(new_id)
        print form.errors
        return HttpResponse("Fail Form")
    return HttpResponse("only POST is possible")

def items(request):
    if request.method == "GET":

        try:
            itemID = request.GET['itemid']
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

def item(request, itemID):
    if request.method == "GET":

        try:
            desc = Description.objects.get(pk=itemID)
            dd = {"desc":str(desc.desc), "quality":str(desc.quality), "rate":str(desc.rate)}
            return HttpResponse(str(dd))
        except:
            return HttpResponse("Fail")

    return HttpResponse("only GET is possible")

def cust_phones(request):
    if request.method == "GET":

        try:
            
            phone = request.GET['phone_num']
            print phone
            cust = Customer.objects.get(pk=phone)
           
            dd = {"name":str(cust.name), "email":str(cust.email)}
            return HttpResponse(str(dd))
        except:
            return HttpResponse("Customer with given phone number not in the database!")

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
            descr = form.cleaned_data['desc']
            billr = form.cleaned_data['bill']
            lengthr = form.cleaned_data['length']
            qualityr = form.cleaned_data['quality']
            rater = form.cleaned_data['rate']
            qrcodestring = descr+"\n"+str(billr)+"\n"+str(lengthr)+"\n"+qualityr+"\n"+str(rater)+"\n"
            img = qrcode.make(qrcodestring)
            #var = "/home/vashisht/shop-pyth/shop-pyth./media"
            filename = new_id+".jpg"
   
        
            img.save('front/media/tests.png','PNG')
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
