from django.conf.urls import url
from pkuxiaoyi.blog.views import index
from django.conf import settings

  
urlpatterns = [ 
    url(r'^static/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_ROOT}),
    url(r'^$',index),
]

 

