from django.shortcuts import render, HttpResponse, HttpResponsePermanentRedirect, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.db.models import Sum
import time, json, pymysql, collections, os, pymongo
from app01.models import *
from django.http import JsonResponse

conn = pymongo.MongoClient("121.201.29.81", 28017)
db = conn.admin  # 连接库
db.authenticate("admin", "daxianggm123")  # 用户认证
db = conn.datashow

from datashow import settings

mysql_host = settings.DATABASES['default']['HOST']
mysql_port = settings.DATABASES['default']['PORT']
mysql_user = settings.DATABASES['default']['USER']
mysql_passwd = settings.DATABASES['default']['PASSWORD']
mysql_db = settings.DATABASES['default']['NAME']


def select_mysql(sql):
    conn = pymysql.connect(host='121.201.68.21', port=3307, user='jiang', passwd='jiangwenhui', db='daxiangzhanshi',

                           charset='UTF8')
    cur = conn.cursor()
    reCount = cur.execute(sql)

    nRet = cur.fetchall()
    cur.close()

    conn.close()
    return nRet


def acc_login(request):
    if request.method == "POST":
        print(request.POST)
        user = authenticate(username=request.POST.get("username"), password=request.POST.get("password"))
        if user:
            login(request, user)
            return redirect('/')
        else:
            error = "error"
            return render(request, "login.html", {"login_error": error})
    print("用户正在访问登陆页")
    return render(request, "login.html")


@login_required
def acc_logout(requrst):
    logout(requrst)
    return redirect("/")


@login_required
def index(request):
    print("用户正在访问主页")
    return render(request, 'index.html')


def ret_dic(filename):
    # 获取json数据并返回
    data = ''
    with open(os.path.join('static/json', filename), encoding='utf-8') as f:
        for i in f:
            data += i
    data = json.loads(data)
    return data


@login_required
def pvuv(request):
    # Day,访问量（PV）,访问用户（UV）
    data = 'Day,访问量（PV）,访问用户（UV）\n'
    dat = 访问量.objects.all()
    for i in dat:
        data += '{},{},{}\n'.format(i.Day, i.PV, i.UV)
    if request.is_ajax():
        return JsonResponse(data, safe=False)
    # return JsonResponse(data, safe=False)
    return render(request, 'pvuv.html')


@login_required
def 可缩放的时间轴(request):
    # 在json文件里面的数据 1370131200000去掉3个0就是时间戳
    # data = []
    # dat = 时间轴.objects.all()
    # for i in dat:
    #     data.append([i.Day, i.val])
    # print(dat)
    data = ret_dic('可缩放的时间轴.json')
    if request.is_ajax():
        return JsonResponse(data, safe=False)
    return render(request, '可缩放的时间轴.html')


@login_required
def 百分比堆叠面积图(request):
    data = db.堆叠面积图.find()
    for i in data:
        dat = i
    dat['_id'] = ''
    # data = ret_dic('堆叠面积图.json')
    if request.is_ajax():
        return JsonResponse(dat, safe=False)
    return render(request, '百分比堆叠面积图.html')


@login_required
def 误差线图(request):
    data = db.误差线图.find()
    for i in data:
        dat = i
    dat['_id'] = ''
    data = dat['data']
    # data = ret_dic('误差线图.json')
    if request.is_ajax():
        return JsonResponse(data, safe=False)
    return render(request, '误差线图.html')


@login_required
def 颜色渐变的饼图(request):
    # data = [
    #     ['Firefox', 45.0],
    #     ['IE', 26.8],
    #     ['Chrome', 12.8],
    #     ['Safari', 8.5],
    #     ['Opera', 6.2],
    #     ['其他', 0.7]
    # ]
    data = db.颜色渐变的饼图.find()
    for i in data:
        dat = i
    dat['_id'] = ''
    data = dat['data']
    if request.is_ajax():
        return JsonResponse(data, safe=False)
    return render(request, '颜色渐变的饼图.html')


@login_required
def 带辅助线的气泡图(request):
    # data = ret_dic('带辅助线的气泡图.json')
    data = db.带辅助线的气泡图.find()
    for i in data:
        dat = i
    dat['_id'] = ''
    data = dat['data']
    if request.is_ajax():
        return JsonResponse(data, safe=False)
    return render(request, '带辅助线的气泡图.html')


@login_required
def 多个图表共用一个提示框(request):
    # data = ret_dic('多个图表共用一个提示框.json')
    data = db.多个图表共用一个提示框.find()
    for i in data:
        dat = i
    dat['_id'] = ''
    if request.is_ajax():
        return JsonResponse(dat, safe=False)
    return render(request, '多个图表共用一个提示框.html')


@login_required
def 混合图堆叠图(request):
    # data = ret_dic('混合图堆叠图.json')
    data = db.混合图堆叠图.find()
    for i in data:
        dat = i
    dat['_id'] = ''
    data = dat
    b = zip(*data["column"])
    c = list(round(sum(i) / len(i), 2) for i in b)
    # print(c)
    data['spline'] = c
    if request.is_ajax():
        return JsonResponse(data, safe=False)
    return render(request, '混合图+堆叠图.html')


@login_required
def 气泡图(requrst):
    data = ret_dic('气泡图.json')
    if requrst.is_ajax():
        return JsonResponse(data, safe=False)
    return render(requrst, '气泡图.html')


@login_required
def 散点图(request):
    data = ret_dic('散点图.json')
    if request.is_ajax():
        return JsonResponse(data, safe=False)
    return render(request, '散点图.html')


def get汇总运维数据():
    pv = int(select_mysql('select pv from app01_zcpvuv order by id desc limit 1')[0][0])
    uv = int(select_mysql('select uv from app01_zcpvuv order by id desc limit 1')[0][0])
    ip = int(select_mysql('select ip from app01_zcpvuv order by id desc limit 1')[0][0])
    order_num = int(select_mysql('select order_num from app01_zcpvuv order by id desc limit 1')[0][0])

    当前HA访问量 = 当前的HA访问量.objects.all().order_by('-times')[0:1]
    for i in 当前HA访问量:
        当前HA访问 = i.value

    告警_情况 = 告警情况.objects.filter(times__gte=time.strftime('%Y-%m-%d'))
    告警的情况 = {}
    for i in 告警_情况:
        # print(i.alerttypeId,i.alertNum)
        告警的情况[i.alerttypeId] = i.alertNum

    服务响应 = 服务响应时间和当前状态.objects.filter(times__gte=time.strftime('%Y-%m-%d')).order_by('-times')[0:3]
    服务响应时间当前状态 = {}
    for i in 服务响应:
        # print(i.服务名称)
        服务响应时间当前状态[i.服务名称] = {"北京探测点响应时间": i.北京探测点响应时间, "上海探测点响应时间": i.上海探测点响应时间,
                              "北京探测点当前状态": i.北京探测点当前状态, "上海探测点当前状态": i.上海探测点当前状态}

    网络情况_ = 网络情况.objects.filter(times__gte=time.strftime('%Y-%m-%d')).order_by('-times')[0:1]
    网络_情况 = {}
    for i in 网络情况_:
        网络_情况['北京网络情况'] = i.北京网络情况
        网络_情况['上海网络情况'] = i.上海网络情况
        网络_情况['广州网络情况'] = i.广州网络情况
        网络_情况['北京网络可用性'] = i.北京网络可用性
        网络_情况['上海网络可用性'] = i.上海网络可用性
        网络_情况['广州网络可用性'] = i.广州网络可用性

    redis_命中率 = redis命中率.objects.filter(times__gte=time.strftime('%Y-%m-%d')).order_by('-times')[0:1]
    redis命中率_ = {}
    for i in redis_命中率:
        # print(i)
        redis命中率_['电商命中率'] = i.电商命中率
        redis命中率_['NET命中率'] = i.NET命中率
        redis命中率_['SSO命中率'] = i.SSO命中率

    青云用量_ = 青云用量.objects.filter(times__gte=time.strftime('%Y-%m-%d')).order_by('-times')[0:1]
    青云_用量 = {}
    for i in 青云用量_:
        青云_用量['云服务器'] = i.云服务器
        青云_用量['路由器'] = i.路由器
        青云_用量['硬盘'] = i.硬盘
        青云_用量['IP地址'] = i.IP地址

    数据库QPS = 当前数据库QPS.objects.filter(times__gte=time.strftime('%Y-%m-%d')).order_by('-times')[0:1]
    数据库QPS_ = {}
    for i in 数据库QPS:
        数据库QPS_['SSOPostgreSQL'] = i.SSOPostgreSQL
        数据库QPS_['电商PostgreSQL'] = i.电商PostgreSQL
        数据库QPS_['SSOMySQL'] = i.SSOMySQL
        数据库QPS_['电商MySQL'] = i.电商MySQL

    七牛用量_ = 七牛用量.objects.filter(times__gte=time.strftime('%Y-%m-%d')).order_by('-times')[0:1]
    七牛_用量 = {}
    for i in 七牛用量_:
        七牛_用量['存储'] = i.存储
        七牛_用量['CDN'] = i.CDN
        七牛_用量['带宽'] = i.带宽

    def select_sql(sql):
        conn = pymysql.connect(host=mysql_host, port=mysql_port, user=mysql_user, passwd=mysql_passwd, db=mysql_db,

                               charset='UTF8')
        cur = conn.cursor()
        reCount = cur.execute(sql)
        nRet = cur.fetchall()
        cur.close()
        conn.close()
        return nRet

    CDN带宽总流量 = select_sql("select sum(value) from app01_cdn_流量 where times>='{}'".format(time.strftime('%Y%m%d')))[0][0]
    CDN带宽总流量 = round(CDN带宽总流量 / 1024 / 1024, 2)
    # print(CDN带宽总流量)
    CDN带宽峰值 = select_sql(
        "select sum(value),times from app01_cdn_带宽 where times>='{}' group by times  order by sum(value) desc limit 1; ".format(
            time.strftime('%Y%m%d')))[0]
    # print(CDN带宽峰值)
    进总流量最大 = \
        select_sql(
            "select value from app01_总流量 where times>=curdate() and in_or_out='in'   order by value desc limit 1")[
            0][0] / 4000000
    进总流量最小 = \
        select_sql(
            "select value from app01_总流量 where times>=curdate() and in_or_out='in'   order by value asc limit 1")[0][
            0] / 4000000
    进总流量最新 = \
        select_sql(
            "select value from app01_总流量 where times>=curdate() and in_or_out='in'   order by times desc limit 1")[
            0][0] / 4000000
    出总流量最大 = \
        select_sql(
            "select value from app01_总流量 where times>=curdate() and in_or_out='out'   order by value desc limit 1")[
            0][0] / 4000000
    出总流量最小 = \
        select_sql(
            "select value from app01_总流量 where times>=curdate() and in_or_out='out'   order by value asc limit 1")[0][
            0] / 4000000
    出总流量最新 = \
        select_sql(
            "select value from app01_总流量 where times>=curdate() and in_or_out='out'   order by times desc limit 1")[
            0][0] / 4000000

    服务器可用率 = 二十四小时服务器可用率.objects.all().order_by('-times')[0:1]
    for i in 服务器可用率:
        服务器可用率_ = i.value

    data = {'pvuvip': [pv, uv, ip, order_num], "当前HA访问量": 当前HA访问, "二十四小时服务器可用率": 服务器可用率_,
            "告警的情况": 告警的情况, "服务响应时间当前状态": 服务响应时间当前状态,
            "网络_情况": 网络_情况, "redis命中率": redis命中率_, "青云用量": 青云_用量,
            "当前数据库QPS": 数据库QPS_, "七牛用量": 七牛_用量, "CDN带宽总流量": CDN带宽总流量,
            "CDN带宽峰值": [round(CDN带宽峰值[0] / 1000, 2),
                        CDN带宽峰值[1][:4] + "-" + CDN带宽峰值[1][4:6] + "-" + CDN带宽峰值[1][6:8] + ' ' + CDN带宽峰值[1][8:10] + ':' +
                        CDN带宽峰值[1][10:]], "总流量": {"进总流量最大": 进总流量最大, "进总流量最小": 进总流量最小, "进总流量最新": 进总流量最新,
                                                  "出总流量最大": 出总流量最大, "出总流量最小": 出总流量最小, "出总流量最新": 出总流量最新, }
            }

    return data


@login_required
def 运维数据汇总平台(request):
    data = get汇总运维数据()
    if request.is_ajax():
        return JsonResponse(data, safe=False)
    return render(request, '运维数据汇总平台.html')


@login_required
def 总流量(request):
    from app01.models import 总流量 as in_or_out
    times = []
    data = [{
        'name': '总流量(进)',
        'data': []
    }, {
        'name': '总流量(出)',
        'data': []
    },
    ]
    dat = in_or_out.objects.filter(times__gte=time.strftime('%Y-%m-%d'))
    for i in dat:
        times.append(i.times[11:])
        if i.in_or_out == 'in':
            data[0]['data'].append(round(i.value / 4000000, 2))
        else:
            data[1]['data'].append(round(i.value / 4000000, 2))
    if request.is_ajax():
        return JsonResponse([times, data], safe=False)

    return render(request, '总流量.html')


@login_required
def CDN带宽(request):
    times = []
    带宽 = []
    流量 = []
    # CDN带宽_ = CDN_带宽.objects.filter(times__gte=time.strftime('%Y%m%d'))
    CDN带宽_ = CDN_带宽.objects.filter(times__gte=time.strftime('%Y%m%d')).values('times').annotate(
        value=Sum('value')).values('times', 'value')
    for i in CDN带宽_:
        times.append(i['times'][-4:-2] + ':' + i['times'][-2:])
        带宽.append(round(i['value'] / 1000, 2))
        # print(i)

    CDN流量_ = CDN_流量.objects.filter(times__gte=time.strftime('%Y%m%d')).values('times').annotate(
        value=Sum('value')).values('times', 'value')
    for i in CDN流量_:
        流量.append(round(i['value'] / 1024 / 1024, 2))
    if request.is_ajax():
        return JsonResponse([times, 带宽, 流量], safe=False)
    return render(request, 'CDN带宽.html')


@login_required
def 最近7天(request):
    times = []
    name = 'name'
    data = 'data'
    dat = [{
        name: 'PV',
        data: []
    }, {
        name: 'UV/万',
        data: []
    }, {
        name: 'IP',
        data: []
    }, {
        name: '订单量',
        data: []
    }]
    sql = "select * from app01_zcpvuv order by id desc limit 12"
    sqldata = select_mysql(sql)
    for i in sqldata:
        # print(i)
        times.append(i[4])
        # dat[0][data].append(i[2])
        dat[1][data].append(i[3] / 10000)
        # dat[2][data].append(i[6])
        dat[3][data].append(i[7])
    times.reverse()
    dat[0][data].reverse()
    dat[1][data].reverse()
    dat[2][data].reverse()
    dat[3][data].reverse()
    if request.is_ajax():
        return JsonResponse([times, dat], safe=False)
    return render(request, '最近7天.html')
