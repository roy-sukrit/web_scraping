from django.shortcuts import render
from database.models import myData



# Create your views here.
def base(request):
    logoData=myData.objects.all()[:300]
    return render(request,'base.html',{'logoData': logoData})


def page2(request):
    logoData=myData.objects.all()[300:600]
    return render(request,'page2.html',{'logoData': logoData})


def page3(request):
     logoData=myData.objects.all()[600:900]
     return render(request,'page3.html',{'logoData': logoData})

def page4(request):
     logoData=myData.objects.all()[900:1000]
     return render(request,'page4.html',{'logoData': logoData})

def page5(request):
     logoData=myData.objects.all()[1000:1500]
     return render(request,'page5.html',{'logoData': logoData})

def page6(request):
     logoData=myData.objects.all()[1500:1600]
     return render(request,'page6.html',{'logoData': logoData})

def page7(request):
     logoData=myData.objects.all()[1600:1700]
     return render(request,'page7.html',{'logoData': logoData})

def page8(request):
     logoData=myData.objects.all()[1700:1795]
     return render(request,'page8.html',{'logoData': logoData})