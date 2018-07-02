#-*- coding: utf-8 -*-
from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt
from django.db import connections

#UTIL
import json
import uuid

from django.conf import settings
from backend.djangoapps.common.views import common_sample
from backend.djangoapps.common.views import dictfetchall

from backend.models import SecretKey

def sessionCheck(request):
    if 'auth' in request.session:
        print("session is ok")
        return 'authSuccess'
    elif 'auth' not in request.session:
        print("session is no")
        return 'authFail'


@csrf_exempt
def login(request):

    if request.is_ajax():
        secretKey = request.POST.get('secretKey')
        print("secretKey = ", secretKey)

        auth = SecretKey.objects.filter(secret_key=secretKey)
        print("len(auth) = ", len(auth))

        if len(auth) == 0:
            return JsonResponse({'return':'fail'})
        else:
            request.session['auth'] = 'true'
            return JsonResponse({'return':'success'})

    return render(request, 'backend/login.html')

def index(request):
    result = sessionCheck(request)
    if result == 'authFail':
        return redirect('/login')

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
    result = sessionCheck(request)
    if result == 'authFail':
        return redirect('/login')

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
            DATE_FORMAT(regist_date, "%Y.%c.%e") as regist_date,
            locate('♡',content) as loc
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

    if max_id[0][0] == None:
        context['max_id'] = 0
    else:
        context['max_id'] = int(max_id[0][0]) + 1

    return render(request, 'backend/checklist.html', context)

def apiChecklistCreate(request):
    result = sessionCheck(request)
    if result == 'authFail':
        return redirect('/login')

    content = request.POST.get('content')

    with connections['default'].cursor() as cur:
        query = '''
            insert into iriyong_todo(content)
            value('{content}')
        '''.format(content=content)
        cur.execute(query)

    return JsonResponse({'return':'success'})

def apiChecklistDelete(request):
    result = sessionCheck(request)
    if result == 'authFail':
        return redirect('/login')

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
    result = sessionCheck(request)
    if result == 'authFail':
        return redirect('/login')

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

def shift(request):
    result = sessionCheck(request)
    if result == 'authFail':
        return redirect('/login')

    context = {}

    return render(request, 'backend/shift.html', context)

@csrf_exempt
def apiMovieCreate(request):
    result = sessionCheck(request)
    if result == 'authFail':
        return redirect('/login')

    movie_name = request.POST.get('movie_name')
    movie_subject = request.POST.get('movie_subject')
    movie_start = request.POST.get('movie_start')
    movie_runtime = request.POST.get('movie_runtime')
    movie_contry = request.POST.get('movie_contry')
    movie_url = request.POST.get('movie_url')
    movie_sumnail = request.POST.get('movie_sumnail')

    with connections['default'].cursor() as cur:
        query = '''
            select id
            from iriyong_file_store
            where file_origin_name = '{movie_sumnail}'
            and delete_yn = 'N'
        '''.format(movie_sumnail=movie_sumnail)
        cur.execute(query)
        file_id = cur.fetchall()

    with connections['default'].cursor() as cur:
        query = '''
            insert into iriyong_movie(
                movie_name,
                movie_subject,
                movie_makedate,
                movie_runtime,
                movie_contry,
                movie_url,
                movie_sumnail)
            value(
                '{movie_name}',
                '{movie_subject}',
                '{movie_start}',
                '{movie_runtime}',
                '{movie_contry}',
                '{movie_url}',
                '{file_id}');
        '''.format(
            movie_name=movie_name,
            movie_subject=movie_subject,
            movie_start=movie_start,
            movie_runtime=movie_runtime,
            movie_contry=movie_contry,
            movie_url=movie_url,
            file_id=file_id[0][0]
        )
        cur.execute(query)

    return JsonResponse({'return':'success'})


def memory(request):
    result = sessionCheck(request)
    if result == 'authFail':
        return redirect('/login')
    context = {}
    return render(request, 'backend/memory.html', context)

def admin(request):
    result = sessionCheck(request)
    if result == 'authFail':
        return redirect('/login')
    context = {}
    return render(request, 'backend/admin.html', context)

def get_file_ext(filename):
    filename_split = filename.split('.')
    file_ext_index = len(filename_split)
    file_ext = filename_split[file_ext_index - 1]
    return file_ext

def common_single_file_upload(file_object):

    UPLOAD_DIR = settings.FILE_UPLOAD

    file_name = str(file_object).strip()
    file_name_enc = str(uuid.uuid4()).replace('-', '')
    file_ext = get_file_ext(file_name).strip()
    file_byte_size = file_object.size
    file_size = str(file_byte_size / 1024) + "KB"
    file_dir = UPLOAD_DIR + file_name_enc + '.' + file_ext

    fp = open(file_dir, 'wb')
    for chunk in file_object.chunks():
        fp.write(chunk)
    fp.close()

    with connections['default'].cursor() as cur:
        query = '''
        INSERT INTO iriyong_file_store
                    (file_origin_name,
                     file_encode_name,
                     file_ext,
                     file_path,
                     file_size)
        VALUES      ('{file_name}',
                     '{file_name_enc}',
                     '{file_ext}',
                     '{UPLOAD_DIR}',
                     '{file_size}')
        '''.format(
            file_name=file_name,
            file_name_enc=file_name_enc,
            file_ext=file_ext,
            UPLOAD_DIR=UPLOAD_DIR,
            file_size=file_size)
        cur.execute(query)

@csrf_exempt
def fileUpload(request):

    if 'file' in request.FILES:
        fileObject = request.FILES['file']
        common_single_file_upload(fileObject)

    return JsonResponse({'a':'b'})

def movie(request):
    result = sessionCheck(request)
    if result == 'authFail':
        return redirect('/login')

    with connections['default'].cursor() as cur:
        query = '''
            SELECT
                a.id,
                a.movie_name,
                a.movie_subject,
                a.movie_makedate,
                a.movie_runtime,
                a.movie_contry,
                a.movie_url,
                concat(b.file_path, b.file_encode_name, '.' ,b.file_ext) as full_path
            FROM iriyong_movie as a
            join iriyong_file_store as b
            on a.movie_sumnail = b.id
            WHERE a.delete_yn = 'N'
            ORDER BY id DESC;
        '''
        cur.execute(query)
        movie_list = cur.fetchall()

    context = {}
    context['movie_list'] = movie_list
    return render(request, 'backend/movie.html', context)

def movieDetail(request, pageId):
    result = sessionCheck(request)
    if result == 'authFail':
        return redirect('/login')

    print("pageId = ", pageId)

    with connections['default'].cursor() as cur:
        query = '''
            select movie_name, movie_url
            from iriyong_movie
            where id = '{pageId}';
        '''.format(pageId=pageId)
        cur.execute(query)
        movie_list = cur.fetchall()

    context = {}
    context['movie_list'] = movie_list
    return render(request, 'backend/movieDetail.html', context)
