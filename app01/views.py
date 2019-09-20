from django.shortcuts import HttpResponse
import json
from app01.spider.spider_class import SpidersXing
from app01.spider.spider_keys import SpidersShop, main
from app01.analysis.ana_class import percentage_xing
from app01.analysis.ana_keys import price_key, discount_key, seller_len
from itertools import chain


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




