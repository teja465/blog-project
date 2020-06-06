from django.shortcuts import render,get_object_or_404
from blog.models import *
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from blog.forms import *
# Create your views here.   PageNotAnInteger



#173

def home_view(request):
    #print(request.path,'im being printed')
    posts=blog_model.objects.filter(status__iexact='published')

    q=request.GET.get('q')
    #print(q,'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
    if q:
        posts=blog_model.objects.filter(title__icontains=q)
        return render(request,'searchresults.html',{'posts':posts})
    paginator=Paginator(posts,3)
    num=request.GET.get('posts')
    try:
        posts=paginator.page(num)
    except EmptyPage:
        posts=paginator.page(num.num_pages)
    except PageNotAnInteger :
        posts=paginator.page(1)



    return render(request,'index.html',{'posts':posts})





def profile_view(request,uname):
    posts=blog_model.objects.filter(author_iexact=uname)
def get_post(request,id):
    print(request.path,'im being printed')
    post=blog_model.objects.get(id=id)
    return render(request,'blogspot.html',{'post':post})
def  write_post(request):
    form=post_form()
    if request.method=='POST':
        data=post_form(request.POST)
        if data.is_valid():
            tt=data.cleaned_data['title']
            print(tt,'title printed vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv')
            data.save(commit=True)
            obj=blog_model.objects.get(title__iexact=tt)
        return HttpResponseRedirect('view_post/{}'.format(obj.id))
    return render(request,'writePost.html',{'form':form})
