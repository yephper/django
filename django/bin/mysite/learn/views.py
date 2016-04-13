#coding:utf-8
from django.shortcuts import render
from django.template.loader import render_to_string
from django.http import HttpResponse,HttpResponseRedirect
from django.views.decorators.cache import cache_page  # 缓存
from django.core.urlresolvers import reverse
import os,json
# 引入我们创建的表单类
from .forms import AddForm


def add(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a)+int(b)
    return HttpResponse(str(c))

def add2(request, a, b):
    c = int(a) + int(b)
    return HttpResponse(str(c))


def old_add2_redirect(request, a, b):
    return HttpResponseRedirect(
        reverse('add2', args=(a, b))
    )


def home(request):
    #info_dict = {'site': u'自强学堂', 'content': u'各种IT技术教程'}
    info_dict = map(str, range(100))# 一个长度为100的 List
    return render(request, 'home.html', {'info_dict': info_dict})



# @cache_page(60 * 15)
def index(request):
    if request.method == 'POST':# 当提交表单时
        form = AddForm(request.POST) # form 包含提交的数据
        if form.is_valid():# 如果提交的数据合法
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            return HttpResponse(str(int(a) + int(b)))

    else:# 当正常访问时
        BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        static_html = BASE_DIR + '/static/page/' + 'static.html';
        form = AddForm()
        if not os.path.exists(static_html):
            content = render_to_string('index.html', form)
            with open(static_html, 'w') as static_file:
                static_file.write(content)

        return render(request, 'index.html', {'form': form})



def sendEmail(request):
    if request.method == 'POST':
        from django.conf import settings
        from django.core.mail import EmailMultiAlternatives

        from_email = settings.DEFAULT_FROM_EMAIL
        # subject 主题 content 内容 to_addr 是一个列表，发送给哪些人
        msg = EmailMultiAlternatives(request.POST['subject'], request.POST['content'], request.POST['from_email'], ['1377157459@qq.com'])
        # 信息内容类型
        msg.content_subtype = "html"
        # 添加附件（可选）
        # msg.attach_file('./twz.png')
        # 发送
        res = msg.send()
        return HttpResponse(res);

    else:
        List = ['自强学堂', '渲染Json到模板']
        Dict = {'site': '自强学堂', 'author': '涂伟忠'}
        return render(request,'send.html',{
            'List': json.dumps(List),
            'Dict': json.dumps(Dict)
        })


def testAjax(request):
    return render(request, 'testajax.html')
