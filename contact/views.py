from django.contrib import messages
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import loader
from .form import contactform
from .models import Contactlist
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='/usermem')
def contacts(request):
    """
    template = loader.get_template('contact/contacts.html')
    return HttpResponse(template.render(request))
    """
    return render(request, 'contact/contacts.html')
@login_required(login_url='/usermem')
def addcontact(request):
    template = loader.get_template('contact/addcontact.html')
    context ={
        'cf': contactform
    }
    return HttpResponse(template.render(context, request))

@login_required(login_url='/usermem')
def postContact(request):
    if request.method == "POST":
        cf = contactform(request.POST)
        if cf.is_valid():
            savecf= Contactlist(
                username = cf.cleaned_data['username'],
                email = cf.cleaned_data['email'],
                body = cf.cleaned_data['body']
            )
            if Contactlist.objects.filter(username=savecf.username).exists():
                
                messages.error(request, 'liên hệ đã tồn tại.')
                return redirect('addcontact')
            else:
                savecf.save()
                messages.success(request, 'thêm liên hệ thành công.')
                return redirect('getcontact')

@login_required(login_url='/usermem')
def getcontact(request):
    template= loader.get_template('contact/getcontact.html')
    contactlist = Contactlist.objects.all().values()
    context = {
        'contactlist':contactlist
    }
    return HttpResponse(template.render(context, request))

