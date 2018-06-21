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

    with connections['default'].cursor() as cur:
        query = '''
            select max(id)
            FROM iriyong_todo
        '''
        cur.execute(query)
        max_id = cur.fetchall()

    with connections['default'].cursor() as cur:
        query = '''
            select id, content,
            DATE_FORMAT(regist_date, "%Y.%c.%e") as regist_date
            FROM iriyong_todo
            where complete = 'N'
            and delete_yn = 'N'
            order by id desc
        '''
        cur.execute(query)
        no_list = cur.fetchall()

    with connections['default'].cursor() as cur:
        query = '''
            select id, content,
            DATE_FORMAT(regist_date, "%Y.%c.%e") as regist_date
            FROM iriyong_todo
            where complete = 'Y'
            and delete_yn = 'N'
            order by id desc
        '''
        cur.execute(query)
        ok_list = cur.fetchall()

    context = {}
    context['ok_list'] = ok_list
    context['no_list'] = no_list
    context['max_id'] = int(max_id[0][0]) + 1
    return render(request, 'backend/checklist.html', context)

def apiChecklistCreate(request):

    content = request.POST.get('content')

    with connections['default'].cursor() as cur:
        query = '''
            insert into iriyong_todo(content)
            value('{content}')
        '''.format(content=content)
        cur.execute(query)

    return JsonResponse({'return':'success'})

def apiChecklistDelete(request):

    boardId = request.POST.get('boardId')
    boardId = boardId.replace('post','')

    with connections['default'].cursor() as cur:
        query = '''
            update iriyong_todo
            set delete_yn = 'Y'
            where id = '{boardId}'
        '''.format(boardId=boardId)
        cur.execute(query)

    return JsonResponse({'return':'success'})

def apiChecklistComplete(request):

    boardId = request.POST.get('boardId')
    boardId = boardId.replace('post','')

    with connections['default'].cursor() as cur:
        query = '''
            update iriyong_todo
            set complete = 'Y'
            where id = '{boardId}'
        '''.format(boardId=boardId)
        cur.execute(query)

    return JsonResponse({'return':'success'})

def memory(request):
    context = {}
    return render(request, 'backend/memory.html', context)

def admin(request):
    context = {}
    return render(request, 'backend/admin.html', context)

def movie(request):

    with connections['default'].cursor() as cur:
        query = '''
            SELECT
                id,
                movie_name,
                movie_subject,
                movie_makedate,
                movie_runtime,
                movie_contry,
                movie_url,
                movie_sumnail
            FROM
                iriyong_movie
            WHERE
                delete_yn = 'N'
            ORDER BY id DESC
        '''
        cur.execute(query)
        movie_list = cur.fetchall()

    context = {}
    context['movie_list'] = movie_list
    return render(request, 'backend/movie.html', context)

def movieDetail(request, pageId):

    print("pageId = ", pageId)

    context = {}
    return render(request, 'backend/movieDetail.html', context)
