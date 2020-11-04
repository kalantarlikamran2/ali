from django.shortcuts import render


# Create your views here.

def sites(request):

    context={



    }

    return render(request,'sites/sites.html',context)