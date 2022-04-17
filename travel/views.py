from django.shortcuts import render,redirect
from .models import Travelguides
# Create your views here.


Travel2=Travelguides()
def submitform(request):
    
    if request.method=='POST':
        Travel1=Travelguides()
        Travel1.name=request.POST['Name']
        Travel1.img=request.FILES['img']
        Travel1.desc=request.POST['desc']
        Travel1.price=request.POST['price']
        offer=request.POST.get('offer_yes')
        if offer=='yes':
            offer=True
        else:
            offer=False
        Travel1.offer=offer

        Travel1.save()
        return redirect('/')
    else:
        return render(request,'travel_provider_Form.html')
# Create your views here.
def Travel(request):
    # Travel2=Travelguides.objects.get(id=3)
    # Travel2.delete()
    Travels=Travelguides.objects.all()
    return render(request,'Travel.html',{'travels':Travels})