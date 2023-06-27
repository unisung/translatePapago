
from django.urls import path
from . import views
from .views import index, index_redirect, index_json, index_file, index_trans, index_trans_result

urlpatterns = [
    #path('', views.index),
    path('', index, name='index'),
    path('redirect', index_redirect, name='index_redirect'),
    path('json', index_json, name='index_json'),
    path('file', index_file, name='index_file'),
    path('trans', index_trans, name='index_trans'),
    path('trans_result', index_trans_result, name='index_trans_result'),
]
