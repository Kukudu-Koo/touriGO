from django.shortcuts import render,redirect
from .models import newss
# Create your views here.



def submitform(request):
    if request.method=='POST':
        news1=newss()
        news1.name=request.POST['Name']
        news1.img=request.FILES['img']
        news1.desc=request.POST['desc']
        news1.save()
        return redirect('/')
    else:
        return render(request,'Blog_Form.html')

def news(request):
    news2=newss.objects.all()
    return render(request,'news.html',{'newss':news2})