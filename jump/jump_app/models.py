from django.db import models

# Create your models here.

class UserInfo(models.Model):
    USER_ROLE=(
        (u'1', u'admin'),
        (u'2', u'user'),
    )
    user = models.CharField(verbose_name="用户名", max_length=32)
    passwd = models.CharField(verbose_name="密码", max_length=32)
    admin = models.CharField(verbose_name="状态", max_length=32, choices=USER_ROLE, default="2")
    def __str__(self):
        return self.user

    class Meta:
        verbose_name_plural = u'用户表'
