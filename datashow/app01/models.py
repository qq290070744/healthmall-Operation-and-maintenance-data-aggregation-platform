from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class userpro(models.Model):
    user = models.OneToOneField(User)
    name = models.CharField(u'姓名', max_length=30)

    def __str__(self):
        return self.name


class 访问量(models.Model):
    Day = models.CharField(max_length=100)
    PV = models.IntegerField()
    UV = models.IntegerField()

    def __str__(self):
        return self.Day


class 时间轴(models.Model):
    Day = models.CharField(max_length=100)
    val = models.FloatField()

    def __str__(self):
        return self.Day


class 总流量(models.Model):
    itemid = models.IntegerField()
    value = models.IntegerField()
    times = models.CharField(max_length=100)
    in_or_out = models.CharField(max_length=100)

    def __str__(self):
        return self.in_or_out


class 当前的HA访问量(models.Model):
    value = models.IntegerField()
    times = models.CharField(max_length=100)

    def __str__(self):
        return self.times


class 告警情况(models.Model):
    alerttypeId = models.IntegerField()
    alerttype = models.CharField(max_length=100)
    alertNum = models.IntegerField()
    times = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.alerttype


class 服务响应时间和当前状态(models.Model):
    服务名称 = models.CharField(max_length=100)
    北京探测点响应时间 = models.CharField(max_length=100)
    上海探测点响应时间 = models.CharField(max_length=100)
    北京探测点当前状态 = models.CharField(max_length=100)
    上海探测点当前状态 = models.CharField(max_length=100)
    times = models.CharField(max_length=100)

    def __str__(self):
        return self.服务名称


class 网络情况(models.Model):
    北京网络情况 = models.CharField(max_length=100)
    上海网络情况 = models.CharField(max_length=100)
    广州网络情况 = models.CharField(max_length=100)
    times = models.CharField(max_length=100)
    北京网络可用性 = models.CharField(max_length=50, null=True)
    上海网络可用性 = models.CharField(max_length=50, null=True)
    广州网络可用性 = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.times


class redis命中率(models.Model):
    电商命中率 = models.CharField(max_length=100)
    NET命中率 = models.CharField(max_length=100)
    SSO命中率 = models.CharField(max_length=100)
    times = models.CharField(max_length=100)

    def __str__(self):
        return self.times


class 青云用量(models.Model):
    云服务器 = models.IntegerField()
    路由器 = models.IntegerField()
    硬盘 = models.IntegerField()
    IP地址 = models.IntegerField()
    times = models.CharField(max_length=100)

    def __str__(self):
        return self.times


class 当前数据库QPS(models.Model):
    SSOPostgreSQL = models.CharField(max_length=100, null=True)
    电商PostgreSQL = models.CharField(max_length=100, null=True)
    SSOMySQL = models.CharField(max_length=100, null=True)
    电商MySQL = models.CharField(max_length=100, null=True)

    times = models.CharField(max_length=100)

    def __str__(self):
        return self.times


class 七牛用量(models.Model):
    存储 = models.CharField(max_length=100)
    CDN = models.CharField(max_length=100)
    带宽 = models.CharField(max_length=100)
    times = models.CharField(max_length=100)

    def __str__(self):
        return self.times


class CDN_带宽(models.Model):
    domain = models.CharField(max_length=100, null=True)
    value = models.IntegerField()
    times = models.CharField(max_length=100)

    def __str__(self):
        return self.domain


class CDN_流量(models.Model):
    domain = models.CharField(max_length=100, null=True)
    value = models.IntegerField()
    times = models.CharField(max_length=100)

    def __str__(self):
        return self.domain


class CDN_回源带宽(models.Model):
    domain = models.CharField(max_length=100, null=True)
    value = models.IntegerField()
    times = models.CharField(max_length=100)

    def __str__(self):
        return self.domain


class 二十四小时服务器可用率(models.Model):
    value = models.CharField(max_length=100)
    times = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.value
