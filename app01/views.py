from django.shortcuts import render, HttpResponse
import json
from django.views import View

# Create your views here.


class Login(View):
    def get(self, request, format=None):
        res = {
            'name': 'konghui'
        }

        res = json.dumps(res)
        return HttpResponse(res)

