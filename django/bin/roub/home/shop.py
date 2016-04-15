from django.shortcuts import render,render_to_response
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from .models import Goods
import json,datetime,MySQLdb
from django.template import RequestContext
from django import forms
from collections import Iterable

class shop(object):

     # 商品列表
    def shopList(request):
        response = Goods.objects.filter(sid='105')[0:10]
        return render(request, 'shop/shopList.html' , {'response':response})


    # 确认订单
    def confirm(request):
        # 获取商品ID
        ids = request.COOKIES['ids']
        ids = ids.split('%2C')
        # 取出商品购买个数
        cart = []
        for i in ids:
            cart.append(request.COOKIES['goods'+i])
        goods = []
        for i in cart:
            goods.append(i.split('_'))
        # 查询商品数据
        gids = []
        for i in goods:
            gids.append(i[0])
        # 执行原声sql
        try:
            sql='SELECT id,gname,goprice FROM home_goods WHERE sid = 105 AND id IN (%s)'
            in_p=', '.join(list(map(lambda x: '%s', gids)))
            sql = sql % in_p
            goodsInfo = Goods.objects.raw(sql, gids)
        except MySQLdb.Error as e:
            return HttpResponse("Mysql Error %d: %s" % (e.args[0], e.args[1]))

        info = {}
        data = []
        for i in goodsInfo:
            for v in goods:
                if i.id == int(v[0]):
                    info['id'] = i.id
                    info['gname'] = i.gname
                    info['buynum'] = int(v[1])
                    info['buyprice'] = i.goprice * int(v[1])
                    data.append(info)

        return HttpResponse(data)
        return render(request, 'shop/confirm.html' , {'goodsInfo':data , 'goods':goods})
