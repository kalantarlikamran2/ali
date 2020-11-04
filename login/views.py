from django.shortcuts import render


# Create your views here.

def list(request):

    context={



    }

    return render(request,'login/login.html',context)