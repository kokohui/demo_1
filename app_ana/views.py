from django.shortcuts import render, HttpResponse, redirect
import json
from app_ana.spider.spider_class import SpidersXing,SpidersXing2
from app_ana.analysis.ana_class import percentage_xing
from app_ana.analysis.ana_keys import price_key, discount_key, seller_len, deliver
from app_ana.spider.spider_shop import SpidersShop
from django.views import View


def spider_category(request):

    if request.method == "POST":
        start_url = request.POST.get('start_url')
        start_url= start_url.split('?')[0]
        spider = SpidersXing(start_url)

        item = {}
        item_1 = spider.parse_xing()

        item_1 = item_1.get('item_tip')
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

        item_all_json = json.dumps(item)

        return HttpResponse(item_all_json)
    return HttpResponse('spdier_category')


def spider_xing_2(request):

    if request.method == "POST":
        start_url = request.POST.get('start_url')
        start_url = 'https://www.lazada.com.my/catalog/?_keyori=ss&from=input&page={}&q=1'.format(start_url)
        spider = SpidersXing2(start_url)

        item = {}
        item_1 = spider.parse_xing()

        item_1 = item_1.get('item_tip')
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

        item_all_json = json.dumps(item)

        return HttpResponse(item_all_json)
    return HttpResponse('spdier_category')


def spider_detail(request):

    if request.method == "POST":
        start_url = request.POST.get('start_url')

        spider = SpidersShop(start_url)
        item_all = spider.parse_pro_2()

        price_list_list = []
        review_list_list = []
        score_list_list = []
        shop_list_list = []
        discount_list_list = []
        percent_list_list = []
        seller_list_list = []
        location_list_list = []

        item_list = item_all.get("commodityInfo")
        for item_data in item_list:
            price_list_list.append(item_data["price"])
            review_list_list.append(item_data['evaNum'])
            score_list_list.append(item_data['score'])
            discount_list_list.append(item_data['discount'])
            shop_list_list.append(item_data['shopSize'])
            location_list_list.append(item_data['location'])

            percent_list_list.append(item_data['percentRate'])
            seller_list_list.append(item_data['sellerKey'])
        item_al = {}
        item_al['item_price'] = price_key(price_list_list)
        item_al['item_review'] = price_key(review_list_list)
        item_al['item_score'] = price_key(score_list_list)
        item_al['item_shop_size'] = price_key(shop_list_list)

        item_al['item_discount'] = discount_key(discount_list_list)
        item_al['item_percent'] = discount_key(percent_list_list)
        item_al['item_sellerName'] = seller_len(seller_list_list)
        item_al['location_list_list'] = deliver(location_list_list)

        item_all['item_ana'] = item_al
        item_list_all = json.dumps(item_all)

        return HttpResponse(item_list_all)
    return HttpResponse('spdier_category')


def spider_shop(request):

    if request.method == "POST":
        start_url = request.POST.get('start_url')
        start_url = start_url.split('?')[0].replace('shop/', '') + '?langFlag=en&q=All-Products&from=wangpu'

        spider = SpidersShop(start_url)
        item_all = spider.parse_pro_2()

        price_list_list = []
        review_list_list = []
        score_list_list = []
        shop_list_list = []
        discount_list_list = []
        percent_list_list = []
        seller_list_list = []
        location_list_list = []

        item_list = item_all.get("commodityInfo")
        for item_data in item_list:
            price_list_list.append(item_data["price"])
            review_list_list.append(item_data['evaNum'])
            score_list_list.append(item_data['score'])
            discount_list_list.append(item_data['discount'])
            shop_list_list.append(item_data['shopSize'])
            location_list_list.append(item_data['location'])

            percent_list_list.append(item_data['percentRate'])
            seller_list_list.append(item_data['sellerKey'])
        item_al = {}
        item_al['item_price'] = price_key(price_list_list)
        item_al['item_review'] = price_key(review_list_list)
        item_al['item_score'] = price_key(score_list_list)
        item_al['item_shop_size'] = price_key(shop_list_list)

        item_al['item_discount'] = discount_key(discount_list_list)
        item_al['item_percent'] = discount_key(percent_list_list)
        item_al['item_sellerName'] = seller_len(seller_list_list)
        item_al['location_list_list'] = deliver(location_list_list)

        item_all['item_ana'] = item_al
        item_list_all = json.dumps(item_all)

        return HttpResponse(item_list_all)
    return HttpResponse('spdier_category')


def spider_keywords(request):

    if request.method == "POST":
        start_url = request.POST.get('start_url')
        start_url = 'https://www.lazada.com.my/catalog/?_keyori=ss&from=input&page={}&q=1'.format(start_url)

        spider = SpidersShop(start_url)
        item_all = spider.parse_pro_2()


        price_list_list = []
        review_list_list = []
        score_list_list = []
        shop_list_list = []
        discount_list_list = []
        percent_list_list = []
        seller_list_list = []
        location_list_list = []

        item_list = item_all.get("commodityInfo")
        for item_data in item_list:
            price_list_list.append(item_data["price"])
            review_list_list.append(item_data['evaNum'])
            score_list_list.append(item_data['score'])
            discount_list_list.append(item_data['discount'])
            shop_list_list.append(item_data['shopSize'])
            location_list_list.append(item_data['location'])

            percent_list_list.append(item_data['percentRate'])
            seller_list_list.append(item_data['sellerKey'])
        item_al = {}
        item_al['item_price'] = price_key(price_list_list)
        item_al['item_review'] = price_key(review_list_list)
        item_al['item_score'] = price_key(score_list_list)
        item_al['item_shop_size'] = price_key(shop_list_list)

        item_al['item_discount'] = discount_key(discount_list_list)
        item_al['item_percent'] = discount_key(percent_list_list)
        item_al['item_sellerName'] = seller_len(seller_list_list)
        item_al['location_list_list'] = deliver(location_list_list)

        item_all['item_ana'] = item_al
        item_list_all = json.dumps(item_all)

        return HttpResponse(item_list_all)
    return HttpResponse('spdier_category')


class Login(View):
    def get(self, request, format=None):
        res = {
            'name': 'konghui'
        }
        # res = json.dumps(res)
        return render(request, 'login.html')


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
        return render(request, '../app_ana/templates/spider.html')


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




