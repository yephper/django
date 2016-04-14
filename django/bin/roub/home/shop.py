from django.shortcuts import render,render_to_response
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from .models import Goods
import json,datetime
from django.template import RequestContext
from django import forms

class shop(object):

     # 商品列表
    def shopList(request):
        response = Goods.objects.filter(sid='105')[0:10]
        return render(request, 'shop/shopList.html' , {'response':response})


    # 确认订单
    def confirm(request):
        # 获取商品ID
        ids = request.COOKIES['ids']
        ids = print(ids).split('%2C')
        # 取出商品购买个数
        for i in ids:
            pass
        return HttpResponse(ids)
