from django.db import models

# Create your models here.
class Users(models.Model):
    username   = models.CharField(max_length=30,unique=True)
    age        = models.IntegerField()
    password   = models.CharField( max_length=128)

    created_at = models.DateTimeField(u'创建时间', auto_now_add=True, editable = True)

    def __str__(self):
        return u"%s (%s, %s)" % (self.username, self.age, self.created_at)






class Goods(models.Model):
    gname         = models.CharField(u'商品名称', max_length=100,unique=True)
    gdescription  = models.CharField(u'商品描述', max_length=200,unique=True)
    gcontent      = models.TextField(u'商品详情')
    cid           = models.IntegerField(u'商品分类id')
    sid           = models.IntegerField(u'分店ID')
    goprice       = models.FloatField(u'原价', max_length=10,unique=True)
    gdprice       = models.FloatField(u'折扣价', max_length=10,unique=True)
    gstock        = models.IntegerField(u'库存', max_length=10,unique=True)
    gimg          = models.CharField(u'商品图片', max_length=200,unique=True)
    pictureset    = models.TextField(u'商品图片集')
    gorder        = models.IntegerField(u'商品排序', max_length=5,unique=True)
    gtype         = models.IntegerField(u'消费类型', max_length=1,unique=True)
    gstatus       = models.IntegerField(u'商品状态', max_length=1,unique=True)
    gvrebate      = models.FloatField(u'VIP会员返现金额', max_length=10)
    printid       = models.CharField(u'打印机ID', max_length=32,unique=True)
    isboutique    = models.IntegerField(u'是否精品', max_length=1,unique=True)


    def __str__(self):
        return u"%s (%s, %s)" % (self.gname, self.gdescription, self.gcontent)
