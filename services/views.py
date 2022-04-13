# Create your views here.
from django.shortcuts import redirect, render

# Create your views here.
def services(request):
    return render(request,'services.html')

