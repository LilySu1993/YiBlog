# coding:utf-8
from django.shortcuts import render
from blog.models import Group, Blog


def index(request):
    # 获取所有的博客分组列表
    group_list = Group.objects.all()
    # 获取所有的博客列表
    new_blog_list = Blog.objects.order_by('-upload_date')[0:5]
    # 获取推荐文章（前5篇）
    rec_blog_list = Blog.objects.order_by('recommend_level')[0:5]
    return render(request, 'blog/index.html', {'group_list': group_list,
                                               'new_blog_list': new_blog_list, 'rec_blog_list': rec_blog_list})


def blog(request):
    # 获取所有的博客分组列表
    group_list = Group.objects.all()
    # 获取所有博客
    blog_list = Blog.objects.all()
    # 获取所有的博客列表
    new_blog_list = Blog.objects.order_by('-upload_date')[0:5]
    # 获取推荐文章（前5篇）
    rec_blog_list = Blog.objects.order_by('recommend_level')[0:5]
    return render(request, 'blog/blog.html', {'group_list': group_list, 'new_blog_list': new_blog_list,
                                              'rec_blog_list': rec_blog_list, 'blog_list': blog_list})


def about(request):
    # 获取所有的博客分组列表
    group_list = Group.objects.all()
    # 获取所有的博客列表
    new_blog_list = Blog.objects.order_by('-upload_date')[0:5]
    # 获取推荐文章（前5篇）
    rec_blog_list = Blog.objects.order_by('recommend_level')[0:5]
    return render(request, 'blog/about.html', {'group_list': group_list,
                                               'new_blog_list': new_blog_list, 'rec_blog_list': rec_blog_list})



