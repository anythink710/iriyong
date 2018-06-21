from django.urls import path
from django.conf.urls import url

from .djangoapps.common import views as CommonViews
from .djangoapps.main import views as MainViews

urlpatterns = [
    # main-url
    url('checklist$', MainViews.checklist, name='checklist'),

    url('apiChecklistCreate$', MainViews.apiChecklistCreate, name='apiChecklistCreate'),
    url('apiChecklistDelete$', MainViews.apiChecklistDelete, name='apiChecklistDelete'),
    url('apiChecklistComplete$', MainViews.apiChecklistComplete, name='apiChecklistComplete'),

    url('checklist$', MainViews.checklist, name='checklist'),
    url('checklist$', MainViews.checklist, name='checklist'),

    url('memory$', MainViews.memory, name='memory'),

    url('movie$', MainViews.movie, name='movie'),
    url('movieDetail/(?P<pageId>[0-9]{1,4})$', MainViews.movieDetail, name='movieDetail'),

    url('admin$', MainViews.admin, name='admin'),

    url('$', MainViews.index, name='index'),
]
