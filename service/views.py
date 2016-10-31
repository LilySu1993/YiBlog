# coding:utf-8
from django.shortcuts import render, HttpResponse, render_to_response, HttpResponseRedirect, HttpResponsePermanentRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.views.decorators.csrf import csrf_exempt
from management.models import Role, User
from blog.models import Group, Blog
import json, time, datetime, os
from PIL import Image


def search(request):
    keyword = request.POST.get('keyword')
    #
    return render(request)


def add_blog(request):
    return render(request)


# 删除某个角色，并将该角色下的所有用户移至‘普通用户’
def delete_role(request):
    if request.is_ajax() and request.method == 'POST':
        role_id = request.POST.get('role_id')
        if role_id is None:
            result = {'status': '0', 'info': '出现错误：待删除的角色ID不能为空！'}
        else:
            try:
                # 删除角色之前，将该角色下的所有用户修改到"普通用户"角色下
                user_list = User.objects.filter(role=role_id)
                default_role = Role.objects.get(role_name='普通用户')
                for user in user_list:
                    user.role = default_role
                    user.save()
                Role.objects.get(id=role_id).delete()
                result = {'status': '1', 'info': '已成功删除该角色！'}
            except ObjectDoesNotExist:
                result = {'status': '1', 'info': '待删除的角色不存在！'}
        return HttpResponse(json.dumps(result), content_type='application/json')
    return render(request, 'role/index.html')


# 删除某个博客
def delete_blog(request):
    if request.is_ajax() and request.method == 'POST':
        blog_id = request.POST.get('blog_id')
        if blog_id is None:
            result = {'status': '0', 'info': '出现错误：待删除的博客ID不能为空！'}
        else:
            try:
                b = Blog.objects.get(id=blog_id)
                # 删除该博客对应的图片
                os.remove(b.image)
                b.delete()
                result = {'status': '1', 'info': '已成功删除该博客！'}
            except ObjectDoesNotExist:
                result = {'status': '1', 'info': '待删除的博客不存在！'}
        return HttpResponse(json.dumps(result), content_type='application/json')
    return render(request, 'blogs/index.html')


# 删除某个分组，并将该分组下的所有博客移至Default分组下
def delete_group(request):
    if request.is_ajax() and request.method == 'POST':
        group_id = request.POST.get('group_id')
        if group_id is None:
            result = {'status': '0', 'info': '出现错误：待删除的分组ID不能为空！'}
        else:
            try:
                # 删除分组之前，首先将该分组下的所有博客的分组修改为Default
                blog_list = Blog.objects.filter(group=group_id)
                default_group = Group.objects.get(group_name='Default')
                for blog in blog_list:
                    blog.group = default_group
                    blog.save()
                Group.objects.get(id=group_id).delete()
                result = {'status': '1', 'info': '已成功删除该分组！'}
            except ObjectDoesNotExist:
                result = {'status': '1', 'info': '待删除的分组不存在！'}
        return HttpResponse(json.dumps(result), content_type='application/json')
    return render(request, 'group/index.html')


# 删除某个用户
def delete_user(request):
    if request.is_ajax() and request.method == 'POST':
        user_id = request.POST.get('user_id')
        if user_id is None:
            result = {'status': '0', 'info': '出现错误：待删除的用户ID不能为空！'}
        else:
            try:
                User.objects.get(id=user_id).delete()
                result = {'status': '1', 'info': '已成功删除该用户！'}
            except ObjectDoesNotExist:
                result = {'status': '1', 'info': '待删除的用户不存在！'}
        return HttpResponse(json.dumps(result), content_type='application/json')
    return render(request, 'user/index.html')


@csrf_exempt
def search_role(request):
    keywords = request.POST['keywords']
    if keywords is None:
        roles = None
    else:
        roles = Role.objects.all().filter(role_name__contains=keywords)
    return render(request, 'role/index.html', {'role_list': roles})


@csrf_exempt
def search_blog(request):
    keywords = request.POST['keywords']
    if keywords is None:
        blogs = None
    else:
        blogs = Blog.objects.all().filter(name__contains=keywords)
    return render(request, 'blogs/index.html', {'blog_list': blogs})


@csrf_exempt
def search_group(request):
    keywords = request.POST['keywords']
    if keywords is None:
        groups = None
    else:
        groups = Group.objects.all().filter(group_name__contains=keywords)
    return render(request, 'group/index.html', {'group_list': groups})


@csrf_exempt
def search_user(request):
    keywords = request.POST['keywords']
    if keywords is None:
        users = None
    else:
        users = User.objects.all().filter(username__contains=keywords)
    return render(request, 'user/index.html', {'user_list': users})


@csrf_exempt
def img_upload(request):
    try:
        reqfile = request.FILES['upload_file']
        img = Image.open(reqfile)
        if img is None:
            result = {'status': '1', 'info': '图片为空！'}
            return HttpResponse(json.dumps(result), content_type='application/json')
        else:
            # 对图片进行等比缩放
            img.thumbnail((500, 500), Image.ANTIALIAS)
            str_time = str(time.mktime(datetime.datetime.now().timetuple()))
            str_time = str_time[:-2]
            url = "static/var/image/" + str_time + ".png"
            # 保存图片
            img.save(url, "png")
            result = {'status': '1', 'info': '图片上传成功！', 'url':url}
            return HttpResponse(json.dumps(result), content_type='application/json')
    except Exception, e:
        result = {'status': '0', 'info': '图片上传出现错误：%s' %e}
        return HttpResponse(json.dumps(result), content_type='application/json')


