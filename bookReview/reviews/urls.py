from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /
    url(r'^$', views.review_list, name='review_list'),
    # ex: /review/5/
    url(r'^review/(?P<review_id>[0-9]+)/$', views.review_detail, name='review_detail'),
    # ex: /Book/
    url(r'^Book$', views.Book_list, name='Book_list'),
    # ex: /Book/5/
    url(r'^Book/(?P<Book_id>[0-9]+)/$', views.Book_detail, name='Book_detail'),
    url(r'^Book/(?P<Book_id>[0-9]+)/add_review/$', views.add_review, name='add_review'),
]