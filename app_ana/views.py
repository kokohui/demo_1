from django.shortcuts import render, HttpResponse, redirect
import json
from app_ana.spider.spider_class import SpidersXing
from app_ana.spider.spider_keys import SpidersShop, main
from app_ana.analysis.ana_class import percentage_xing
from app_ana.analysis.ana_keys import price_key, discount_key, seller_len
from itertools import chain
from django.views import View


def spider_category(request):

    if request.method == "POST":
        start_url = request.POST.get('start_url')
        spider = SpidersXing(start_url)

        item = {}
        item_1 = spider.parse_xing()
        item_2 = {}
        tips = item_1.get('tips')
        percentage_1 = percentage_xing(tips, item_1.get('tips_1'))
        percentage_2 = percentage_xing(tips, item_1.get('tips_2'))
        percentage_3 = percentage_xing(tips, item_1.get('tips_3'))
        percentage_4 = percentage_xing(tips, item_1.get('tips_4'))
        percentage_5 = percentage_xing(tips, item_1.get('tips_5'))
        item_2['percentage_1'] = percentage_1
        item_2['percentage_2'] = percentage_2
        item_2['percentage_3'] = percentage_3
        item_2['percentage_4'] = percentage_4
        item_2['percentage_5'] = percentage_5
        item['tip'] = item_1
        item['percentage'] = item_2

        item = json.dumps(item)
        print(item)

        return HttpResponse(item)
    return HttpResponse('spdier_category')


def spider_keyword(request):
    if request.method == "POST":
        keyword = request.POST.get('keyword')
        pags = request.POST.get('pags')
        if pags == None:
            pags = 2

        price_list_list = []
        review_list_list = []
        discount_list_list = []
        percentRate_list_list = []
        sellerName_list_list = []

        item_list = main(int(pags), keyword)
        for item_data in item_list:
            price_list_list.append(item_data['price_list'])
            review_list_list.append(item_data['review_list'])
            discount_list_list.append(item_data['discount_list'])
            percentRate_list_list.append(item_data['percentRate_list'])
            sellerName_list_list.append(item_data['sellerName_list'])
        item_al = {}
        item_al['item_price'] = price_key(sum(price_list_list, []))
        item_al['item_review'] = price_key(sum(review_list_list, []))
        item_al['item_discount'] = discount_key(sum(discount_list_list, []))
        item_al['item_percent'] = discount_key(sum(percentRate_list_list, []))
        item_al['item_sellerName'] = seller_len(sum(sellerName_list_list, []))
        item_list_all = json.dumps(item_al)
        return HttpResponse(item_list_all)

    return HttpResponse('spdier_keyword')

class Login(View):
    def get(self, request, format=None):
        res = {
            'name': 'konghui'
        }
        # res = json.dumps(res)
        return render(request,'login.html')

class Index(View):
    def get(self, request, format=None):
        res = {
            "code": 0,
            "msg": "ok",
            "data": {
                "token": "nepadmin-token-test",
                "user": {
                    "username": "小明"
                }
            }
        }

        res = json.dumps(res)
        return HttpResponse(res)

class Spider(View):
    def get(self, request, format=None):
        res = {
            'name': 'konghui'
        }
        res = json.dumps(res)
        return render(request, 'spider.html')

class Menu(View):
    def get(self, request, format=None):
        res = {
                "code": 0,
                "msg": "ok",
                "data": [{
                    "title":"类目选品",
                    "icon": "layui-icon-home",
                    "href": "/spider"
                },{
                    "title":"关键词选品",
                    "icon": "layui-icon-unorderedlist",
                    "href": "/spider"
                },{
                    "title":"店铺选品",
                    "icon": "layui-icon-container",
                    "href": "/spider"
                }]
            }
        res = json.dumps(res)
        return HttpResponse(res)

class Goods(View):
    def get(self, request, format=None):
        res = {
            "code": 0,
            "msg": "ok",
            "count":100,
            "data": [{
                "title":"索尼/Sony PlayStation 4 PS4游戏机 Pro主机 家用电视游戏机国行",
                "thumb": "http://img.alicdn.com/imgextra/i4/2318796651/TB1kNHaw5MnBKNjSZFoXXbOSFXa_!!0-item_pic.jpg_60x60q90.jpg",
                "price":"2999",
                "params":[{
                    "name":"颜色分类",
                    "val":"PS4 Pro 黑色"
                },{
                    "name":"套餐",
                    "val":"单机标配"
                },{
                    "name":"版本类型",
                    "val":"中国大陆"
                }],
                "status":"WAIT_PAY",
                "buycount": "1",
                "time":"2018/09/12 12:23:11"
            },{
                "title":"索尼/Sony PlayStation 4 PS4游戏机 Pro主机 家用电视游戏机国行",
                "thumb": "http://img.alicdn.com/imgextra/i4/2318796651/TB1kNHaw5MnBKNjSZFoXXbOSFXa_!!0-item_pic.jpg_60x60q90.jpg",
                "price":"2999",
                "params":[{
                    "name":"颜色分类",
                    "val":"PS4 Pro 黑色"
                },{
                    "name":"套餐",
                    "val":"单机标配"
                },{
                    "name":"版本类型",
                    "val":"中国大陆"
                }],
                "status":"WAIT_PAY",
                "buycount": "1",
                "time":"2018/09/12 12:23:11"
            },{
                "title":"索尼/Sony PlayStation 4 PS4游戏机 Pro主机 家用电视游戏机国行",
                "thumb": "http://img.alicdn.com/imgextra/i4/2318796651/TB1kNHaw5MnBKNjSZFoXXbOSFXa_!!0-item_pic.jpg_60x60q90.jpg",
                "price":"2999",
                "params":[{
                    "name":"颜色分类",
                    "val":"PS4 Pro 黑色"
                },{
                    "name":"套餐",
                    "val":"单机标配"
                },{
                    "name":"版本类型",
                    "val":"中国大陆"
                }],
                "status":"WAIT_DELIVER",
                "buycount": "1",
                "time":"2018/09/12 12:23:11"
            },{
                "title":"索尼/Sony PlayStation 4 PS4游戏机 Pro主机 家用电视游戏机国行",
                "thumb": "http://img.alicdn.com/imgextra/i4/2318796651/TB1kNHaw5MnBKNjSZFoXXbOSFXa_!!0-item_pic.jpg_60x60q90.jpg",
                "price":"2999",
                "params":[{
                    "name":"颜色分类",
                    "val":"PS4 Pro 黑色"
                },{
                    "name":"套餐",
                    "val":"单机标配"
                },{
                    "name":"版本类型",
                    "val":"中国大陆"
                }],
                "status":"WAIT_REFUND",
                "buycount": "1",
                "time":"2018/09/12 12:23:11"
            },{
                "title":"索尼/Sony PlayStation 4 PS4游戏机 Pro主机 家用电视游戏机国行",
                "thumb": "http://img.alicdn.com/imgextra/i4/2318796651/TB1kNHaw5MnBKNjSZFoXXbOSFXa_!!0-item_pic.jpg_60x60q90.jpg",
                "price":"2999",
                "params":[{
                    "name":"颜色分类",
                    "val":"PS4 Pro 黑色"
                },{
                    "name":"套餐",
                    "val":"单机标配"
                },{
                    "name":"版本类型",
                    "val":"中国大陆"
                }],
                "status":"WAIT_PAY",
                "buycount": "1",
                "time":"2018/09/12 12:23:11"
            },{
                "title":"索尼/Sony PlayStation 4 PS4游戏机 Pro主机 家用电视游戏机国行",
                "thumb": "http://img.alicdn.com/imgextra/i4/2318796651/TB1kNHaw5MnBKNjSZFoXXbOSFXa_!!0-item_pic.jpg_60x60q90.jpg",
                "price":"2999",
                "params":[{
                    "name":"颜色分类",
                    "val":"PS4 Pro 黑色"
                },{
                    "name":"套餐",
                    "val":"单机标配"
                },{
                    "name":"版本类型",
                    "val":"中国大陆"
                }],
                "status":"WAIT_REFUND",
                "buycount": "1",
                "time":"2018/09/12 12:23:11"
            },{
                "title":"索尼/Sony PlayStation 4 PS4游戏机 Pro主机 家用电视游戏机国行",
                "thumb": "http://img.alicdn.com/imgextra/i4/2318796651/TB1kNHaw5MnBKNjSZFoXXbOSFXa_!!0-item_pic.jpg_60x60q90.jpg",
                "price":"2999",
                "params":[{
                    "name":"颜色分类",
                    "val":"PS4 Pro 黑色"
                },{
                    "name":"套餐",
                    "val":"单机标配"
                },{
                    "name":"版本类型",
                    "val":"中国大陆"
                }],
                "status":"WAIT_PAY",
                "buycount": "1",
                "time":"2018/09/12 12:23:11"
            },{
                "title":"索尼/Sony PlayStation 4 PS4游戏机 Pro主机 家用电视游戏机国行",
                "thumb": "http://img.alicdn.com/imgextra/i4/2318796651/TB1kNHaw5MnBKNjSZFoXXbOSFXa_!!0-item_pic.jpg_60x60q90.jpg",
                "price":"2999",
                "params":[{
                    "name":"颜色分类",
                    "val":"PS4 Pro 黑色"
                },{
                    "name":"套餐",
                    "val":"单机标配"
                },{
                    "name":"版本类型",
                    "val":"中国大陆"
                }],
                "status":"WAIT_PAY",
                "buycount": "1",
                "time":"2018/09/12 12:23:11"
            },{
                "title":"索尼/Sony PlayStation 4 PS4游戏机 Pro主机 家用电视游戏机国行",
                "thumb": "http://img.alicdn.com/imgextra/i4/2318796651/TB1kNHaw5MnBKNjSZFoXXbOSFXa_!!0-item_pic.jpg_60x60q90.jpg",
                "price":"2999",
                "params":[{
                    "name":"颜色分类",
                    "val":"PS4 Pro 黑色"
                },{
                    "name":"套餐",
                    "val":"单机标配"
                },{
                    "name":"版本类型",
                    "val":"中国大陆"
                }],
                "status":"WAIT_REFUND",
                "buycount": "1",
                "time":"2018/09/12 12:23:11"
            },{
                "title":"索尼/Sony PlayStation 4 PS4游戏机 Pro主机 家用电视游戏机国行",
                "thumb": "http://img.alicdn.com/imgextra/i4/2318796651/TB1kNHaw5MnBKNjSZFoXXbOSFXa_!!0-item_pic.jpg_60x60q90.jpg",
                "price":"2999",
                "params":[{
                    "name":"颜色分类",
                    "val":"PS4 Pro 黑色"
                },{
                    "name":"套餐",
                    "val":"单机标配"
                },{
                    "name":"版本类型",
                    "val":"中国大陆"
                }],
                "status":"WAIT_PAY",
                "buycount": "1",
                "time":"2018/09/12 12:23:11"
            },{
                "title":"索尼/Sony PlayStation 4 PS4游戏机 Pro主机 家用电视游戏机国行",
                "thumb": "http://img.alicdn.com/imgextra/i4/2318796651/TB1kNHaw5MnBKNjSZFoXXbOSFXa_!!0-item_pic.jpg_60x60q90.jpg",
                "price":"2999",
                "params":[{
                    "name":"颜色分类",
                    "val":"PS4 Pro 黑色"
                },{
                    "name":"套餐",
                    "val":"单机标配"
                },{
                    "name":"版本类型",
                    "val":"中国大陆"
                }],
                "status":"WAIT_PAY",
                "buycount": "1",
                "time":"2018/09/12 12:23:11"
            },{
                "title":"索尼/Sony PlayStation 4 PS4游戏机 Pro主机 家用电视游戏机国行",
                "thumb": "http://img.alicdn.com/imgextra/i4/2318796651/TB1kNHaw5MnBKNjSZFoXXbOSFXa_!!0-item_pic.jpg_60x60q90.jpg",
                "price":"2999",
                "params":[{
                    "name":"颜色分类",
                    "val":"PS4 Pro 黑色"
                },{
                    "name":"套餐",
                    "val":"单机标配"
                },{
                    "name":"版本类型",
                    "val":"中国大陆"
                }],
                "status":"WAIT_PAY",
                "buycount": "1",
                "time":"2018/09/12 12:23:11"
            },{
                "title":"索尼/Sony PlayStation 4 PS4游戏机 Pro主机 家用电视游戏机国行",
                "thumb": "http://img.alicdn.com/imgextra/i4/2318796651/TB1kNHaw5MnBKNjSZFoXXbOSFXa_!!0-item_pic.jpg_60x60q90.jpg",
                "price":"2999",
                "params":[{
                    "name":"颜色分类",
                    "val":"PS4 Pro 黑色"
                },{
                    "name":"套餐",
                    "val":"单机标配"
                },{
                    "name":"版本类型",
                    "val":"中国大陆"
                }],
                "status":"WAIT_PAY",
                "buycount": "1",
                "time":"2018/09/12 12:23:11"
            },{
                "title":"索尼/Sony PlayStation 4 PS4游戏机 Pro主机 家用电视游戏机国行",
                "thumb": "http://img.alicdn.com/imgextra/i4/2318796651/TB1kNHaw5MnBKNjSZFoXXbOSFXa_!!0-item_pic.jpg_60x60q90.jpg",
                "price":"2999",
                "params":[{
                    "name":"颜色分类",
                    "val":"PS4 Pro 黑色"
                },{
                    "name":"套餐",
                    "val":"单机标配"
                },{
                    "name":"版本类型",
                    "val":"中国大陆"
                }],
                "status":"WAIT_PAY",
                "buycount": "1",
                "time":"2018/09/12 12:23:11"
            },{
                "title":"索尼/Sony PlayStation 4 PS4游戏机 Pro主机 家用电视游戏机国行",
                "thumb": "http://img.alicdn.com/imgextra/i4/2318796651/TB1kNHaw5MnBKNjSZFoXXbOSFXa_!!0-item_pic.jpg_60x60q90.jpg",
                "price":"2999",
                "params":[{
                    "name":"颜色分类",
                    "val":"PS4 Pro 黑色"
                },{
                    "name":"套餐",
                    "val":"单机标配"
                },{
                    "name":"版本类型",
                    "val":"中国大陆"
                }],
                "status":"WAIT_PAY",
                "buycount": "1",
                "time":"2018/09/12 12:23:11"
            },{
                "title":"索尼/Sony PlayStation 4 PS4游戏机 Pro主机 家用电视游戏机国行",
                "thumb": "http://img.alicdn.com/imgextra/i4/2318796651/TB1kNHaw5MnBKNjSZFoXXbOSFXa_!!0-item_pic.jpg_60x60q90.jpg",
                "price":"2999",
                "params":[{
                    "name":"颜色分类",
                    "val":"PS4 Pro 黑色"
                },{
                    "name":"套餐",
                    "val":"单机标配"
                },{
                    "name":"版本类型",
                    "val":"中国大陆"
                }],
                "status":"WAIT_PAY",
                "buycount": "1",
                "time":"2018/09/12 12:23:11"
            },{
                "title":"索尼/Sony PlayStation 4 PS4游戏机 Pro主机 家用电视游戏机国行",
                "thumb": "http://img.alicdn.com/imgextra/i4/2318796651/TB1kNHaw5MnBKNjSZFoXXbOSFXa_!!0-item_pic.jpg_60x60q90.jpg",
                "price":"2999",
                "params":[{
                    "name":"颜色分类",
                    "val":"PS4 Pro 黑色"
                },{
                    "name":"套餐",
                    "val":"单机标配"
                },{
                    "name":"版本类型",
                    "val":"中国大陆"
                }],
                "status":"WAIT_PAY",
                "buycount": "1",
                "time":"2018/09/12 12:23:11"
            },{
                "title":"索尼/Sony PlayStation 4 PS4游戏机 Pro主机 家用电视游戏机国行",
                "thumb": "http://img.alicdn.com/imgextra/i4/2318796651/TB1kNHaw5MnBKNjSZFoXXbOSFXa_!!0-item_pic.jpg_60x60q90.jpg",
                "price":"2999",
                "params":[{
                    "name":"颜色分类",
                    "val":"PS4 Pro 黑色"
                },{
                    "name":"套餐",
                    "val":"单机标配"
                },{
                    "name":"版本类型",
                    "val":"中国大陆"
                }],
                "status":"WAIT_PAY",
                "buycount": "1",
                "time":"2018/09/12 12:23:11"
            },{
                "title":"索尼/Sony PlayStation 4 PS4游戏机 Pro主机 家用电视游戏机国行",
                "thumb": "http://img.alicdn.com/imgextra/i4/2318796651/TB1kNHaw5MnBKNjSZFoXXbOSFXa_!!0-item_pic.jpg_60x60q90.jpg",
                "price":"2999",
                "params":[{
                    "name":"颜色分类",
                    "val":"PS4 Pro 黑色"
                },{
                    "name":"套餐",
                    "val":"单机标配"
                },{
                    "name":"版本类型",
                    "val":"中国大陆"
                }],
                "status":"WAIT_PAY",
                "buycount": "1",
                "time":"2018/09/12 12:23:11"
            },{
                "title":"索尼/Sony PlayStation 4 PS4游戏机 Pro主机 家用电视游戏机国行",
                "thumb": "http://img.alicdn.com/imgextra/i4/2318796651/TB1kNHaw5MnBKNjSZFoXXbOSFXa_!!0-item_pic.jpg_60x60q90.jpg",
                "price":"2999",
                "params":[{
                    "name":"颜色分类",
                    "val":"PS4 Pro 黑色"
                },{
                    "name":"套餐",
                    "val":"单机标配"
                },{
                    "name":"版本类型",
                    "val":"中国大陆"
                }],
                "status":"WAIT_PAY",
                "buycount": "1",
                "time":"2018/09/12 12:23:11"
            },{
                "title":"索尼/Sony PlayStation 4 PS4游戏机 Pro主机 家用电视游戏机国行",
                "thumb": "http://img.alicdn.com/imgextra/i4/2318796651/TB1kNHaw5MnBKNjSZFoXXbOSFXa_!!0-item_pic.jpg_60x60q90.jpg",
                "price":"2999",
                "params":[{
                    "name":"颜色分类",
                    "val":"PS4 Pro 黑色"
                },{
                    "name":"套餐",
                    "val":"单机标配"
                },{
                    "name":"版本类型",
                    "val":"中国大陆"
                }],
                "status":"WAIT_PAY",
                "buycount": "1",
                "time":"2018/09/12 12:23:11"
            },{
                "title":"索尼/Sony PlayStation 4 PS4游戏机 Pro主机 家用电视游戏机国行",
                "thumb": "http://img.alicdn.com/imgextra/i4/2318796651/TB1kNHaw5MnBKNjSZFoXXbOSFXa_!!0-item_pic.jpg_60x60q90.jpg",
                "price":"2999",
                "params":[{
                    "name":"颜色分类",
                    "val":"PS4 Pro 黑色"
                },{
                    "name":"套餐",
                    "val":"单机标配"
                },{
                    "name":"版本类型",
                    "val":"中国大陆"
                }],
                "status":"WAIT_PAY",
                "buycount": "1",
                "time":"2018/09/12 12:23:11"
            }]
        }

        res = json.dumps(res)
        return HttpResponse(res)




