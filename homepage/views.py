from django.shortcuts import render,redirect
from .models import destinations
from homepage import models
# Create your views here.


def submitform(request):
    if request.method=='POST':
        dest1=destinations()
        dest1.name=request.POST['Name']
        dest1.img=request.FILES['img']
        dest1.desc=request.POST['desc']
        dest1.link=request.POST['link']
        dest1.price=request.POST['price']
        offer=request.POST.get('offer_yes')
        if offer=='yes':
            offer=True
        else:
            offer=False
        dest1.offer=offer
        dest1.save()
        return redirect('/')
    else:
        return render(request,'provider_Form.html')

def homepage(request):
    dests=destinations.objects.all()
    return render(request,'index.html',{'dests':dests})