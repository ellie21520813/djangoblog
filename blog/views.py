from django.contrib import messages
from django.shortcuts import redirect, render
from django.template import loader
from django.http import HttpResponse
from .form import imageblogform
#from .models import imageblogmodel
from home.models import post_blog
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
# Create your views here.
@login_required(login_url='/usermem')
def blog(request):
    template = loader.get_template('blog/getblog.html')
    listblog = post_blog.objects.filter(author_blog = request.user).order_by('-created_on')
    count = listblog.count()
    paginator = Paginator(listblog, 2)  # Show 25 contacts per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    me=request.user
    context = {
        'page_obj':page_obj,
        'count':count,
        'me' : me
    }
    return HttpResponse(template.render(context, request))

@login_required(login_url='/usermem')
def postblog(request):
    postblogform = imageblogform(request.POST, request.FILES)
    if postblogform.is_valid():
        saveplf = post_blog(
            title_blog = postblogform.cleaned_data['blog_title'],
            blog_image = postblogform.cleaned_data['blog_image'],
            content_blog = postblogform.cleaned_data['blog_body'],
            author_blog=request.user,

        )
        saveplf.save()
        messages.success(request, "thêm blog thành công")
        return redirect('blog')
    else:
        messages.error(request, 'fail')
        return redirect('blog')
@login_required(login_url='/usermem')
def addblog(request):
    template = loader.get_template('blog/addblog.html')
    context = {
        'ibf':imageblogform
    }
    #return render(request, 'blog/blog.html')
    return HttpResponse(template.render(context, request))


