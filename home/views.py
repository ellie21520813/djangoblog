from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render
from django.template import loader
from django.http import HttpResponse
from .form import imageblogform, commentform
#from .models import imageblogmodel
from .models import post_blog, Comment
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

# Create your views here.
@login_required(login_url='/usermem')
def homelog(request):
    template = loader.get_template('home/home.html')
    listblog = post_blog.objects.all().order_by('-created_on')
    paginator = Paginator(listblog, 2)  # Show 25 contacts per page.
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj':page_obj
    }
    return HttpResponse(template.render(context, request))
@login_required(login_url='/usermem')
def detailpost(request, id):
    #detailx= post_blog.objects.get(id = id)
    #template = loader.get_template('home/detailblog.html')
    detailx = get_object_or_404(post_blog, id=id)
    comments = detailx.comments.all().values().order_by('-created_on')
    cmf = commentform
    if request.method == 'POST':
        cmf = commentform(request.POST)
        if cmf.is_valid():
            savecm= Comment(
                post= detailx,
                name = request.user,
                body = cmf.cleaned_data['body'],

            )
            savecm.save()
    content ={
            'detail': detailx,
            'post': detailx,
            'comments': comments,
            'comment_form': cmf,
            'user': request.user}

    return render(request, 'home/detailblog.html', content)



"""def commentget(request, id):
    template = loader.get_template('home/commentget.html')
    blog= post_blog.objects.get(id=id)
    context={
        'blog':blog,
        'user':request.user,
        'commentform':commentform

    }
    return HttpResponse(template.render(context, request))


def commentpost(request):
    if request.method == "POST":
        cmf = commentform(request.POST)
        if cmf.is_valid():
            savecmf = Comment(
                post = cmf.cleaned_data['name']
            )
    return HttpResponse("hi")
"""
"""
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
    template = loader.get_template('home/home.html')
    context = {
        'ibf':imageblogform
    }
    #return render(request, 'blog/blog.html')
    return HttpResponse(template.render(context, request))


"""