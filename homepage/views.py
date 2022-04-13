from django.shortcuts import render,redirect
from .models import destination
from homepage import models
# Create your views here.


dest1=destination()
dest2=destination()
def submitform(request):
    if request.method=='POST':
        dest1.name=request.POST['Name']
        dest1.img=request.FILES['img']
        dest1.desc=request.POST['desc']
        dest1.link=request.POST['link']
        dest1.price=request.POST['price']
        offer=request.POST.get('offer_yes')
        if offer=='on':
            offer=True
        else:
            offer=False
        dest1.offer=offer

        dest1.save()
        return redirect('/')
    else:
        return render(request,'provider_Form.html')

def homepage(request):
    dests=destination.objects.all()
    return render(request,'index.html',{'dests':dests})