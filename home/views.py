from django.shortcuts import render,HttpResponse


def home_view(request):
    
    context = {
        'isim' : 'Furkan'
    }
    
    return render(request,'home.html',context)
# Create your views here.
