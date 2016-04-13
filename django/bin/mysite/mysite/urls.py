"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import urls as auth_urls
from learn import views as learn_views  # new
admin.autodiscover()

urlpatterns = [
    url(r'^$', learn_views.index, name='index'),
    url(r'^send/', learn_views.sendEmail, name='send'),
    url(r'^add/', learn_views.add, name='add'),  # 注意修改了这一行
    url(r'^add2/(\d+)/(\d+)/$', learn_views.old_add2_redirect),
    url(r'^new_add/(\d+)/(\d+)/$', learn_views.add2, name='add2'),
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('users.urls')),
    url(r'^testajax/', learn_views.testAjax, name='testajax'),
]
