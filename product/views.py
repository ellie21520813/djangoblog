from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url='/usermem')
def listproduct(request):
    """
        template = loader.get_template('product/product.html')
    return HttpResponse(template.render(request))
    """
    return render(request, 'product/product.html')

