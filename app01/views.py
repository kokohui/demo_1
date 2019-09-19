from django.shortcuts import HttpResponse
import json
from app01.spider.spider_class import SpidersXing
from app01.spider.spider_keys import SpidersShop, main
from app01.analysis.ana_class import percentage_xing


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
        print(keyword, pags)

        item = main(int(pags), keyword)

        item = json.dumps(item)
        print(item)

        return HttpResponse(item)

    return HttpResponse('spdier_keyword')




