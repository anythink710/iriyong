#-*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.db import connections

#UTIL
import json

from django.conf import settings
from backend.djangoapps.common.views import common_sample
from backend.djangoapps.common.views import dictfetchall

def index(request):

    """
    making logic
    """

    """
    with connections['default'].cursor() as cur:
        query = '''
            select *
            FROM table
            where sample = '{page}'
        '''.format(page=page)
        cur.execute(query)
        rows = cur.fetchall()
    """

    context = {}
    context['sample_key'] = 'sample_val'

    return render(request, 'backend/index.html', context)

def checklist(request):
    context = {}
    return render(request, 'backend/checklist.html', context)

def memory(request):
    context = {}
    return render(request, 'backend/memory.html', context)

def movie(request):
    context = {}
    return render(request, 'backend/movie.html', context)

def movieDetail(request):
    context = {}
    return render(request, 'backend/movieDetail.html', context)
