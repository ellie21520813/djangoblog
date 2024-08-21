from django.contrib import messages
from django.shortcuts import redirect, render
from django.http import HttpResponse
from .form import Registerform, loginform
from django.template import loader
from django.contrib.auth.models import User
from django.views import View
from django.contrib.auth import authenticate, login, logout
# Create your views here.
class registeruser(View):
    def get(self, request):
        template = loader.get_template('usermem/register.html')
        context ={
            'rgf': Registerform
        }
        return HttpResponse(template.render(context, request))

    def post(self, request):
        username = request.POST['username']
        email =  request.POST['email']
        password = request.POST['password']
        if User.objects.filter(username=username).exists() or User.objects.filter(email=email) :
            messages.error(request, 'Username, email đã tồn tại, vui lòng chọn username, email khác.')
            return redirect('registeruser')
        user= User.objects.create_user(username, email, password)
        user.save()
        return redirect('login')
class loginpage(View):
    def get(self, request):
        template = loader.get_template('usermem/login.html')
        context = {
            'lgp': loginform
        }
        return HttpResponse(template.render(context, request))
    def post(self, request):
        username = request.POST['username']
        password = request.POST['password']
        """
        try:
            user = authenticate(request, username=User.objects.get(email=username), password = password )
        except:
        """
        user = authenticate(request, username=username, password = password )
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            if User.objects.filter(username=username):
                messages.warning(request, "Mật khẩu không đúng")
                return redirect('login')
            else:
                messages.error(request, "Tên đăng nhập hoặc mật khẩu không đúng")
                return redirect('login')
def logoutuser(request):
    logout(request)
    template = loader.get_template('usermem/login.html')
    context = {
        'lgp': loginform
    }
    return HttpResponse(template.render(context, request))
