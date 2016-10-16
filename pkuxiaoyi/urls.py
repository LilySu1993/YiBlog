# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', include('pkuxiaoyi.blog.urls')),
    url(r'^blogs$', 'pkuxiaoyi.blog.views.blogs'),
    url(r'^about$', 'pkuxiaoyi.blog.views.about'),
]
