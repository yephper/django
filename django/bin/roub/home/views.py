from django.shortcuts import render,render_to_response
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from .models import Users
import json,datetime
from django.template import RequestContext
from django import forms

# Create your views here.
class home(object):
    def __init__(request, ):
        mid = request.COOKIES["uid"];
        if mid == '':
            return HttpResponseRedirect('views/login');


    def index(request):
        return render(request, 'views/index.html', {'request': request})

    # 登录
    # #
    def login(request , hour=0):
        if request.method == 'POST':
            username = request.POST['username'];
            password = request.POST['pwd'];
            response = ""

            try:
                response = Users.objects.get(username=username , password=password);
            except:
                return HttpResponse("Error:%s or %r is not exit" %(username,password))
            finally:
                if response == '':
                    return HttpResponseRedirect('login')        # 失败跳转登录
                else:
                    responset = HttpResponseRedirect('index')       # 成功跳转

                    dt = datetime.datetime.now() + datetime.timedelta(hours = int(hour))
                    responset.set_cookie("uid",response.id,expires=dt)
                    return responset

        else:
            data = {'title':"登录" , 'content':"实验"}
            return render(request, 'views/login.html' , {'data':data})


    #退出
    def logout(request):
        response = HttpResponseRedirect('views/index')
        #清理cookie里保存username
        response.delete_cookie('uid')
        return response


    #注册
    def regist(req):
        if req.method == 'POST':
            uf = UserForm(req.POST)
            if uf.is_valid():
                #获得表单数据
                username = uf.cleaned_data['username']
                password = uf.cleaned_data['password']
                #添加到数据库
                Users.objects.create(username= username,password=password)
                return HttpResponse('regist success!!')
        else:
            uf = UserForm()
        return render_to_response('views/regist.html',{'uf':uf}, context_instance=RequestContext(req))


    # 须知
    def xdxz(request):
        return render(request, 'views/xdxz.html' , {'request':request})

    # 服务介绍
    def fwjs(self):
        return render(self, 'views/fwjs.html' , {'self':self})

    # 留言
    def feedback(self):
        return render(self, 'views/feedback.html' , {'self':self})





#表单
class UserForm(forms.Form):
    username = forms.CharField(label='用户名',max_length=100)
    password = forms.CharField(label='密码',widget=forms.PasswordInput())
