"""roub URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.conf import settings
from django.contrib import admin
from django.views import static  #路径调用
from home import views,shop

urlpatterns = [
    url(r'^$', views.home.index,name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^login', views.home.login , name='login'),
    url(r'^regist', views.home.regist , name='regist'),
    url(r'^logout', views.home.logout , name='logout'),
    url(r'^xdxz', views.home.xdxz , name='xdxz'),
    url(r'^fwjs', views.home.fwjs , name='fwjs'),
    url(r'^feedback', views.home.feedback , name='feedback'),
    url(r'^shopList', shop.shop.shopList , name='shopList'),
    url(r'^confirm', shop.shop.confirm , name='confirm'),
    url(r'^sendOrder', shop.shop.sendOrder , name='sendOrder'),
    url(r'^myOrder', shop.shop.myOrder , name='myOrder'),
    url(r'^static_url/(?P<path>.*)$',static.serve,{'document_root':settings.STATIC_PATH}),   # css,js,img 路径
]
