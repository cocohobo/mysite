from myblog.models import Classes, SiteInfo, UserInfo
from django.shortcuts import render

# Create your views here.
def index(request):
    classes = Classes.objects.all()
    siteinfo = SiteInfo.objects.all()[0]
    userList = UserInfo.objects.all()
    data={
        'siteinfo':siteinfo,
        'classes':classes,
        'userList':userList
    }
    return render(request,'index.html',data)
def classes(request):
    classes = Classes.objects.all()
    siteinfo = SiteInfo.objects.all()[0]

    choose_id = request.GET['id']
    choosed = Classes.objects.filter(id = choose_id)
    userList = UserInfo.objects.filter(belong = choosed[0])
    data={
        'siteinfo':siteinfo,
        'classes':classes,
        'userList':userList
    }
    return render(request,'classes.html',data)