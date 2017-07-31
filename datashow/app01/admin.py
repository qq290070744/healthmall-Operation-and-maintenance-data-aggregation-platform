from django.contrib import admin
from .models import *


# Register your models here.
class userproAdmin(admin.ModelAdmin):
    list_display = ('user', 'name',)


admin.site.register(userpro, userproAdmin)


class 访问量Admin(admin.ModelAdmin):
    list_display = ('Day', 'PV', 'UV',)


admin.site.register(访问量, 访问量Admin)


class 时间轴Admin(admin.ModelAdmin):
    list_display = ('Day', 'val',)


admin.site.register(时间轴, 时间轴Admin)


class 总流量Admin(admin.ModelAdmin):
    list_display = ('itemid', 'value', 'in_or_out', 'times')


admin.site.register(总流量, 总流量Admin)


class 当前的HA访问量Admin(admin.ModelAdmin):
    list_display = ('value', 'times')


admin.site.register(当前的HA访问量, 当前的HA访问量Admin)


class 告警情况Admin(admin.ModelAdmin):
    list_display = ('alerttypeId', 'alerttype', 'alertNum', 'times')


admin.site.register(告警情况, 告警情况Admin)


class 服务响应时间和当前状态Admin(admin.ModelAdmin):
    list_display = ('服务名称', '北京探测点响应时间', '上海探测点响应时间', '北京探测点当前状态', '上海探测点当前状态', 'times')


admin.site.register(服务响应时间和当前状态, 服务响应时间和当前状态Admin)


class 网络情况Admin(admin.ModelAdmin):
    list_display = ('北京网络情况', '上海网络情况', '广州网络情况', '北京网络可用性', '上海网络可用性', '广州网络可用性', 'times')


admin.site.register(网络情况, 网络情况Admin)


class 青云用量Admin(admin.ModelAdmin):
    list_display = ('云服务器', '路由器', '硬盘', 'IP地址', 'times',)


admin.site.register(青云用量, 青云用量Admin)


class redis命中率Admin(admin.ModelAdmin):
    list_display = ('电商命中率', 'NET命中率', 'SSO命中率', 'times',)


admin.site.register(redis命中率, redis命中率Admin)


class 当前数据库QPSAdmin(admin.ModelAdmin):
    list_display = ('SSOPostgreSQL', '电商PostgreSQL','SSOMySQL','电商MySQL', 'times',)


admin.site.register(当前数据库QPS, 当前数据库QPSAdmin)


class 七牛用量Admin(admin.ModelAdmin):
    list_display = ('存储', 'CDN', '带宽', 'times',)


admin.site.register(七牛用量, 七牛用量Admin)


class CDN_带宽Admin(admin.ModelAdmin):
    list_display = ('domain', 'value', 'times',)


admin.site.register(CDN_带宽, CDN_带宽Admin)


class CDN_流量Admin(admin.ModelAdmin):
    list_display = ('domain', 'value', 'times',)


admin.site.register(CDN_流量, CDN_流量Admin)


class CDN_回源带宽Admin(admin.ModelAdmin):
    list_display = ('domain', 'value', 'times',)


admin.site.register(CDN_回源带宽, CDN_回源带宽Admin)
