#-*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_protect, csrf_exempt
from django.db import connections
import json

def keyboard(request):

    return JsonResponse({
        'type':'buttons',
        'buttons':['후쿠오카 날씨','오빠 만나는 날']
    })

@csrf_exempt
def answer(request):

    json_str = ((request.body).decode('utf-8'))
    received_json_data = json.loads(json_str)
    datacontent = received_json_data['content']

    if datacontent == '후쿠오카 날씨':
        today = "아직 만들고 있는 중이에요! 언제 비올지 알려드릴게요 ^^"

        return JsonResponse({
                'message': {
                    'text': today
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['후쿠오카 날씨','오빠 만나는 날']
                }

            })

    elif datacontent == '오빠 만나는 날':
        tomorrow = "아직 만들고 있는 중이에요!"

        return JsonResponse({
                'message': {
                    'text': tomorrow
                },
                'keyboard': {
                    'type':'buttons',
                    'buttons':['후쿠오카 날씨','오빠 만나는 날']
                }

            })
