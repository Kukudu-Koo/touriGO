from django.shortcuts import render,redirect
from .models import Tourguides
# Create your views here.



def submitform(request):
    if request.method=='POST':
        tour1=Tourguides()
        tour1.name=request.POST['Name']
        tour1.img=request.FILES['img']
        tour1.desc=request.POST['desc']
        tour1.price=request.POST['price']
        offer=request.POST.get('offer_yes')
        if offer=='yes':
            offer=True
        else:
            offer=False
        tour1.offer=offer

        tour1.save()
        return redirect('/')
    else:
        return render(request,'tour_provider_Form.html')

def tour(request):
    tours=Tourguides.objects.all()
    return render(request,'tour.html',{'tours':tours})