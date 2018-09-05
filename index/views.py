import json

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from index.models import User


def index_view(request):
    return render(request,"index.html")

def login_view(request):
    return render(request,"login.html")

def register_view(request):
    return render(request,"register.html")

def uphonec_view(request):
    '''
    检查手机号是否在数据库存在
    :param request:
    :return:
    '''
    uphone = request.POST['uphone']

    ulist = User.objects.filter(uphone = uphone)

    if ulist:
        # 如果条件未真，则表示手机号码已经存在
        # 响应 status为0,用于通知客户端手机号码已存在
        # 响应 text 值为 "手机号码已存在"
        dic = {
            "status":"0",
            "text":'手机号码已存在'
        }
    else:
        dic = {
            "status" : "1",
            "text" : "可以注册"
        }
    return HttpResponse(json.dumps(dic))