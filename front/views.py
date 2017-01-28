'''
Views for the app
'''
from django.template.loader import render_to_string
from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.core.cache import cache
from .models import Description, Bill, Customer, Sale, Discount
from .forms import DForm, BForm, SForm, CForm
#from shop.settings import MEDIA_URL
#import qrcode
# Create your views here.

def home(request):
    '''Link for Landing Page'''
    context = {}
    return render(request, 'front/home.html', context)

def itemparty(request,name):
    if request.method == "GET":
        try:
           cust = Bill.objects.filter(phone=name)
           context = {'cust': cust}
           return HttpResponse(render_to_string('front/bill.html', context))
           
        except:
           raise Http404("NO PURCHASE ON THE GIVEN DATE EXISTS")
        raise Http404("Only GET supported")


def purchasedate(request, date1, date2):
    '''Stats'''
    if request.method == "GET":
        try:
            ids1 = date1.split("-")
            search1 = "".join(ids1[::-1])
            ids2 = date2.split("-")
            ids2[-1] = str(int(ids2[-1])+1)
            search2 = "".join(ids2[::-1])
            cust = Bill.objects.filter(id__gte=search1+"0", id__lt=search2+"0")
            context = {'cust' : cust}
            return HttpResponse(render_to_string('front/purch.html', context))
            #return render(request, 'front/purch.html', context)
        except Bill.DoesNotExist:
            raise Http404("NO PURCHASE ON THE GIVEN DATE EXISTS")
    raise Http404("Only GET supported")

def custdate(request, date1, date2):
    '''Stats'''
    if request.method == "GET":
        try:
            ids1 = date1.split("-")
            search1 = "".join(ids1[::-1])
            ids2 = date2.split("-")
            ids2[-1] = str(int(ids2[-1])+1)
            search2 = "".join(ids2[::-1])
            cust = Sale.objects.filter(id__gte=search1+"0", id__lt=search2+"0")
            context = {'cust' : cust}
            return HttpResponse(render_to_string('front/date.html', context))
        except Sale.DoesNotExist:
            raise Http404("NO SALE ON THE GIVEN DATE EXISTS")
    raise Http404("Only GET supported")

def index(request):
    '''Link for Landing Page'''
    context = {}
    return render(request, 'front/index.html', context)

def sale(request):
    '''Link for sale Page'''
    context = {'disc':discount()}
    return render(request, 'front/sale.html', context)

def custbill(request, phone):
    '''Get customer info'''
    if request.method == "GET":
        try:
            print phone
            cust = Sale.objects.filter(cust_id=phone)
            context = {'cust': cust}
            return HttpResponse(render_to_string('front/orders.html', context))
        except Customer.DoesNotExist:
            raise Http404("No Sale for the customer exists")
    raise Http404("Only GET supported")

def commitcust(request):
    '''store customer info'''
    if request.method == "POST":
        form = CForm(request.POST)
        if form.is_valid():
            customer = form.save()
            return HttpResponse(str(customer.phone))
        print form.errors
        return HttpResponse("Fail")
    raise Http404("Only POST supported")

def commitsale(request):
    '''store sale info'''
    if request.method == "POST":
        form = SForm(request.POST)
        if form.is_valid():

            #idr = form.cleaned_data['item_id']
            #lengthr = form.cleaned_data['length']
            #custidr = form.cleaned_data['cust_id']
            #qrdata = str(idr)+"\n"+str(lengthr)+"\n"+str(custidr)+"\n"
            #img = qrcode.make(qrdata)
            sale_form = form.save(commit=False)
            new_id = cache.get('today')+str(cache.get('sale'))
            #var = "front/templates/front/Billimg/"+str(new_id)+".png"
            #img.save(var,'PNG')

            item_id = sale_form.item_id.split(",")
            length = sale_form.length.split(",")

            for i in range(0, len(item_id)):
                desc = Description.objects.get(id=item_id[i])
                desc.length -= int(length[i])
                desc.save()

            disc = Discount.objects.get(pk=sale_form.discount)
            disc.count -= 1
            disc.save()

            cache.set('sale', int(str(cache.get('sale')))+1, None)
            sale_form.id = new_id
            sale_form.save()
            return HttpResponse(new_id)
        print form.errors
        return HttpResponse("Fail Form")
    raise Http404("Only POST supported")

def items(request, itemID):
    '''fetch item info'''
    if request.method == "GET":
        try:
            desc = Description.objects.get(pk=itemID)
            item_desc = {"desc":str(desc.desc), "quality":str(desc.quality), "rate":str(desc.rate)}
            return HttpResponse(str(item_desc))
        except:
            return HttpResponse("Fail")
    raise Http404("Only GET supported")

def cust_phone(request, phone):
    if request.method == "GET":
        try:
            cust = Customer.objects.get(pk=phone)
            cust_desc = {"name":str(cust.name), "email":str(cust.email)}
            return HttpResponse(str(cust_desc))
        except:
            return HttpResponse("Fail")
    raise Http404("Only GET supported")

def item(request, itemID):
    if request.method == "GET":
        try:
            desc = Description.objects.get(pk=itemID)
            item_desc = {"desc":str(desc.desc), "quality":str(desc.quality), "rate":str(desc.rate), "length":str(desc.length)}
            return HttpResponse(str(item_desc))
        except:
            return HttpResponse("Fail")
    raise Http404("Only GET supported")

def cust_phones(request, phone):
    if request.method == "GET":
        try:
            cust = Customer.objects.get(pk=phone)
            cust_desc = {"name":str(cust.name), "email":str(cust.email)}
            return HttpResponse(str(cust_desc))
        except:
            return HttpResponse("Customer with given phone number not in the database!")
    raise Http404("Only GET supported")

def commitvalues(request):
    if request.method == "POST":
        form = DForm(request.POST)
        if form.is_valid():
            description = form.save(commit=False)
            new_id = cache.get('today')+str(cache.get('description'))
            cache.set('description',int(str(cache.get('description')))+1, None)
            description.id = new_id
            description.save()
            '''
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
            '''
            return HttpResponse(new_id)
        print form.errors
        return HttpResponse("Fail")
    raise Http404("Only POST supported")

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
    raise Http404("Only POST supported")

def discount():
    discounts = Discount.objects.all()
    disc = []
    for d in discounts:
        if d.count > 0:
            disc += [str(d.value)]
    return disc

def handle_uploaded_image(iid,f):
    with open('front/media/'+iid+f.__str__(), 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    destination.close()
