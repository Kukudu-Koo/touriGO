from django.shortcuts import render,redirect
from .models import hotels
# Create your views here.
hotel2=hotels()
def submitform(request):
    if request.method=='POST':
        hotel1=hotels()
        hotel1.name=request.POST['Name']
        hotel1.img=request.FILES['img']
        hotel1.desc=request.POST['desc']
        hotel1.price=request.POST['price']
        offer=request.POST.get('offer_yes')
        if offer=='yes':
            offer=True
        else:
            offer=False
        hotel1.offer=offer

        hotel1.save()
        return redirect('/')
    else:
        return render(request,'Restaurant_provider_Form.html')
# Create your views here.
def restaurants(request):
    # hotel2=hotels.objects.get(id=3)
    # hotel2.delete()
    hotel=hotels.objects.all()
    return render(request,'Restaurants.html',{'hotel':hotel})