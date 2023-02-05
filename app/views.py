from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse

# Create your views here.

def u_defined_validators(request):
    nfo=NameForm()
    d={'form':nfo}

    if request.method=='POST':
        fd=NameForm(request.POST)
        if fd.is_valid():
            return HttpResponse(str(fd.cleaned_data))



    return render(request,'u_defined_validators.html',d)
