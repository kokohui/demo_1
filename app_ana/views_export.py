from app_ana.spider.spider_class import SpidersXing,SpidersXing2
from app_ana.analysis.ana_class import percentage_xing
from app_ana.analysis.ana_keys import price_key, discount_key, seller_len, deliver
from app_ana.spider.spider_shop import SpidersShop
from django.views import View
from app_ana import models
from xlwt import *
import os
from io import StringIO, BytesIO
from django.shortcuts import render, HttpResponse, redirect
import json


def ExportXing(request):
    if request.method == "GET":
        create_by = request.GET.get('create_by')
        data_json = models.BusStar.objects.filter(create_by=create_by).values('json')

        data_data = list(data_json)[0]['json']
        data_data = json.loads(data_data)

        ws = Workbook(encoding='utf-8')
        w = ws.add_sheet(u'星级数据报表')
        w.write(0, 0, "名称")
        w.write(0, 1, "总星")
        w.write(0, 2, "一星")
        w.write(0, 3, "二星")
        w.write(0, 4, "三星")
        w.write(0, 5, "四星")
        w.write(0, 6, "五星")
        w.write(0, 7, "一星百分比")
        w.write(0, 8, "二星百分比")
        w.write(0, 9, "三星百分比")
        w.write(0, 10, "四星百分比")
        w.write(0, 11, "五星百分比")

        w.write(1, 1, '数据')
        w.write(1, 1, data_data["tip"]["tips"])
        w.write(1, 2, data_data["tip"]["tips_1"])
        w.write(1, 3, data_data["tip"]["tips_2"])
        w.write(1, 4, data_data["tip"]["tips_3"])
        w.write(1, 5, data_data["tip"]["tips_4"])
        w.write(1, 6, data_data["tip"]["tips_5"])
        w.write(1, 7, data_data["percentage"]["percentage_1"])
        w.write(1, 8, data_data["percentage"]["percentage_1"])
        w.write(1, 9, data_data["percentage"]["percentage_1"])
        w.write(1, 10, data_data["percentage"]["percentage_1"])
        w.write(1, 11, data_data["percentage"]["percentage_1"])

        exist_file = os.path.exists(r"星级数据报表.xls")
        if exist_file:
            os.remove("星级数据报表.xls")
        ws.save("星级数据报表.xls")

        sio = BytesIO()
        ws.save(sio)
        sio.seek(0)

        response = HttpResponse(sio.getvalue(), content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename=星级数据报表.xls'
        response.write(sio.getvalue())
        return response


def ExportDetail(request):
    if request.method == "GET":
        create_by = request.GET.get('create_by')
        print(create_by)
        data_json = models.BusProd.objects.filter(create_by=create_by).values()
        print(data_json)
        data_data = list(data_json)

        ws = Workbook(encoding='utf-8')
        w = ws.add_sheet(u'数据报表')
        ww = ws.add_sheet(u'数据分析报表')

        w.write(0, 0, "名称")
        w.write(0, 1, "品牌")
        w.write(0, 2, "标题")
        w.write(0, 3, "促销价")
        w.write(0, 4, "评论数")
        w.write(0, 5, "商品图片链接")
        w.write(0, 6, "折扣比")
        w.write(0, 7, "路径")
        w.write(0, 8, "发货地")
        w.write(0, 9, "商品好评率")
        w.write(0, 10, "店铺年限(月)")
        w.write(0, 11, "店铺等级")
        w.write(0, 12, "店铺名称")
        w.write(0, 13, "店铺链接")
        w.write(0, 14, "店铺好评率")

        ww.write(0, 1, "价格")
        ww.write(0, 2, "评论数")
        ww.write(0, 3, "店铺等级")
        ww.write(0, 4, "折扣比")
        ww.write(0, 5, "好评率")
        ww.write(0, 6, "店铺总数")
        ww.write(0, 7, "中国发货占比")
        ww.write(1, 0, "最高")
        ww.write(2, 0, "最低")
        ww.write(3, 0, "平均")

        num = 1
        for info in data_data:
            # print('info', info, type(info))
            # info = json.loads(info)
            w.write(num, 0, "数据")
            w.write(num, 1, info["brand"])
            w.write(num, 2, info["title"])
            w.write(num, 3, info["price"])
            w.write(num, 4, info["eva_num"])
            w.write(num, 5, info["pro_url"])
            w.write(num, 6, info["discount"])
            w.write(num, 7, info["class_info"])
            w.write(num, 8, info["location"])
            w.write(num, 9, info["percent_rate"])
            w.write(num, 10, info["keep_time"])
            w.write(num, 11, info["shop_size"])
            w.write(num, 12, info["seller_key"])
            w.write(num, 13, info["con_home_url"])
            w.write(num, 14, info["shop_rating"])
            num += 1

        data_ana_data = data_data[0]["item_ana_json"]
        data_ana_data = json.loads(data_ana_data)

        ww.write(1, 1, data_ana_data["item_price"]["max"])
        ww.write(2, 1, data_ana_data["item_price"]["min"])
        ww.write(3, 1, data_ana_data["item_price"]["avg"])
        ww.write(1, 2, data_ana_data["item_review"]["max"])
        ww.write(2, 2, data_ana_data["item_review"]["min"])
        ww.write(3, 2, data_ana_data["item_review"]["avg"])
        ww.write(1, 3, data_ana_data["item_score"]["max"])
        ww.write(2, 3, data_ana_data["item_score"]["min"])
        ww.write(3, 3, data_ana_data["item_score"]["avg"])
        ww.write(1, 4, data_ana_data["item_discount"]["max"])
        ww.write(2, 4, data_ana_data["item_discount"]["min"])
        ww.write(3, 4, data_ana_data["item_discount"]["avg"])
        ww.write(1, 5, data_ana_data["item_percent"]["max"])
        ww.write(2, 5, data_ana_data["item_percent"]["min"])
        ww.write(3, 5, data_ana_data["item_percent"]["avg"])

        ww.write(1, 6, data_ana_data["item_sellerName"])
        ww.write(1, 7, data_ana_data["location_list_list"])

        exist_file = os.path.exists(r"数据报表.xls")
        if exist_file:
            os.remove("数据报表.xls")
        ws.save("数据报表.xls")

        sio = BytesIO()
        ws.save(sio)
        sio.seek(0)

        response = HttpResponse(sio.getvalue(), content_type='application/vnd.ms-excel')
        response['Content-Disposition'] = 'attachment; filename=数据报表.xls'
        response.write(sio.getvalue())

        return response