from django.urls import path
from django.conf.urls import url

from .djangoapps.common import views as CommonViews
from .djangoapps.main import views as MainViews

urlpatterns = [
    # main-url
    url('checklist$', MainViews.checklist, name='checklist'),
    url('memory$', MainViews.memory, name='memory'),
    url('movie$', MainViews.movie, name='movie'),
    url('movieDetail$', MainViews.movieDetail, name='movieDetail'),
    url('$', MainViews.index, name='index'),
]
