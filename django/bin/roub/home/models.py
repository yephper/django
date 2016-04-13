from django.db import models

# Create your models here.
class Users(models.Model):
    username   = models.CharField(max_length=30,unique=True)
    age        = models.IntegerField()
    password   = models.CharField( max_length=128)

    created_at = models.DateTimeField(u'创建时间', auto_now_add=True, editable = True)

    def __str__(self):
        return u"%s (%s, %s)" % (self.username, self.age, self.created_at)


