import json

from django.http import HttpResponse
from django.shortcuts import render, redirect

# Create your views here.
from index.models import User


def index_view(request):
    return render(request,"index.html")

def login_view(request):
    # 如果是post的情况
    if request.method == "POST":
        uphone = request.POST['uphone']
        upwd = request.POST['upwd']

        ulist = User.objects.filter(uphone = uphone,upwd = upwd)
        # 登录成功
        if ulist :
            print(ulist)
            request.session['uphone'] = ulist[0].uphone
            request.session['uid'] = ulist[0].id

            if 'isSaved' in request.POST:
                # 勾选了记住密码
                resp = redirect("/")
                resp.set_cookie(key ="uid",value=ulist[0].id,expires=60*60*24*30)
                resp.set_cookie(key = "uphone",value = ulist[0].uphone,expires=60*60*24*30)
                return resp
            else:
                return redirect("/")
        else:
            # 显示失败原因
            print('密码错误')
            return redirect("/login")

    # 如果是get的情况
    else:
        if "uid" in request.session and "uphone" in request.session:
            print("session有数据")
            return redirect("/")
        else:
            if "uid" in request.COOKIES and 'uphone' in request.COOKIES:
                uid = request.COOKIES['uid']
                uphone = request.COOKIES['uphone']
                request.session['uid'] = uid
                request.session['uphone'] = uphone
                return redirect('/')

            else:
                return render(request,"login.html")



def register_view(request):
    if request.method == "GET":
        return render(request,"register.html")
    else:
        # 实现注册的功能
        uphone = request.POST["uphone"]
        upwd = request.POST['upwd']
        uname = request.POST["uname"]
        uemail = request.POST['email']

        dict  = {
            "uphone":uphone,
            "upwd": upwd,
            "uname" : uname,
            "uemail" : uemail
        }

        # 保存进数据库
        users = User(**dict).save()

        u = User.objects.get(uphone = uphone)

        # 将用户id和uphone保存进session

        request.session['uid'] = u.id
        request.session['uphone'] = u.uphone

        return redirect("/")

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