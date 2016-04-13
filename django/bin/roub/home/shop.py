from django.shortcuts import render,render_to_response
from django.http import HttpResponse,JsonResponse,HttpResponseRedirect
from .models import Users
import json,datetime
from django.template import RequestContext
from django import forms

class shop(object):

     # 商品列表
    def shopList(self):
        return render(self, 'shop/shopList.html' , {'self':self})
