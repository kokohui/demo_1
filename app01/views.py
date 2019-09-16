from django.shortcuts import render, HttpResponse, redirect
import json
from .spider import SpidersXing


def spider_post(request):

    if request.method == "POST":
        start_url = request.POST.get('start_url')
        spider = SpidersXing(start_url)
        item = spider.parse_xing()
        item = json.dumps(item)
        print(item)

        return HttpResponse(item)





