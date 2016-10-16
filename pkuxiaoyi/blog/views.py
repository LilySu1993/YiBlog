# -*-coding:utf-8 -*-

from django.template import loader, Context
from django.http import HttpResponse
from pkuxiaoyi.blog.models import BlogPost

def blogs(request):
    posts = BlogPost.objects.all()
    t = loader.get_template("blogs.html")
    c = Context({'posts':posts})
    return HttpResponse(t.render(c))


def index(request):
    posts = BlogPost.objects.all()
    t = loader.get_template("index.html")
    c = Context({'posts':posts})
    return HttpResponse(t.render(c))
 
def about(request):
    t = loader.get_template("about.html")
    c = Context()
    return HttpResponse(t.render(c))

