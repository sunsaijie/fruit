from django.db import models

# Create your models here.

class User(models.Model):
    uname = models.CharField(max_length=20,verbose_name='姓名')
    upwd = models.CharField(max_length=20,verbose_name="密码")
    uphone = models.CharField(max_length=20,null=True,verbose_name="电话号码")
    uemail = models.EmailField(null=True,verbose_name="电子邮件")
    isActive = models.BooleanField(default=True,verbose_name='激活')

    def __str__(self):
        return self.uphone
