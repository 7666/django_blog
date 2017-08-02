# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.paginator import Paginator, InvalidPage, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from models import *
from django.contrib import auth
from django.contrib.auth.decorators import login_required,permission_required
from django.contrib.auth.hashers import make_password
from forms import *
from django.http import HttpResponse,HttpResponseRedirect
from django.db.models import Count

# Create your views here.
def global_setting(request):
        category_list = Category.objects.all()
        SITE_NAME = Site.objects.get(id = 1).name
        SITE_DESC = Site.objects.get(id = 1).desc
        click_article_list = Article.objects.order_by('-click_count')[:5]
        tag_list = Tag.objects.all()
        ad_list = Ad.objects.all()
        recommend_article_list = Article.objects.all().filter(is_recommend = True)[:5]
        #评论排行
        comment_count_list = Comment.objects.values('article').annotate(comment_count=Count('article')).order_by('-comment_count')
        comment_article_list = [Article.objects.get(pk=comment['article']) for comment in comment_count_list]
        link_list = Link.objects.all()
        archive_list = Article.objects.distinct_date()
        return locals()

def pag(request,article_list):
        paginator = Paginator(article_list, 5)
        try:
            page = int(request.GET.get('page',1))
            article_list = paginator.page(page)
        except (EmptyPage, InvalidPage, PageNotAnInteger):
            article_list = paginator.page(1)
        return article_list


def index(request):
    article_list = Article.objects.all()
    article_list = pag(request, article_list)
    return render(request,'index.html',locals())

def category(request):
    category_id = request.GET.get('cid',None)
    print category_id
    category = Category.objects.get(pk = category_id)
    article_list = category.article_set.all()
    article_list = Article.objects.filter(category=category)
    paginator = Paginator(article_list, 5)
    try:
        page = int(request.GET.get('page',1))
        print page
        article_list = paginator.page(page)
    except (EmptyPage, InvalidPage, PageNotAnInteger):
        article_list = paginator.page(1)
    return render(request,'category.html',locals())


def tag(request):
    tag = request.GET.get('tag','')
    tag1 = Tag.objects.get(name = tag)
    article_list = tag1.article_set.all()
    paginator = Paginator(article_list, 5)
    try:
        page = int(request.GET.get('page',1))
        article_list = paginator.page(page)
    except (EmptyPage, InvalidPage, PageNotAnInteger):
        article_list = paginator.pag(1)
    return render(request,'tag.html',locals())

def article(request):
    article_id = request.GET.get('id',None)
    try:
        article = Article.objects.get(id = article_id)
        print article.category.name
        comment_list = article.comment_set.all()
        comment_counts = comment_list.count()
    except:
        return render(request,'failure.html',{reason:'对不起,没有这个页面'})
    try:
        if request.user.is_authenticated():
            post = User.objects.get(username=request.user)
            post.username = str(post.username)
            post.email = str(post.email)
            post.url = str(post.siteurl)
            comment_form = CommentForm(initial ={'author':post.username,'email':post.email,'url':post.url})
        else:
            comment_form = CommentForm()

        if request.method == 'POST':
                comment_form = CommentForm(request.POST)
                if comment_form.is_valid():
                    cd = comment_form.cleaned_data
                    if request.user.is_authenticated():
                        dic = {'user':request.user,'username':cd['author'],'email':cd['email'],'url':cd['url'],'content':cd['comment'],'article':article}
                    else:
                        dic = {'username':cd['author'],'email':cd['email'],'url':cd['url'],'content':cd['comment'],'article':article}
                    Comment.objects.create(**dic)
                    print 'hello'

    except:
        print 'cuo'

    return render(request,'article.html',locals())

def reg(request):
    try:
        if request.method == 'POST':
            reg_form = RegForm(request.POST)
            if reg_form.is_valid():
                cd = reg_form.cleaned_data
                User.objects.create(username=cd['username'],password=make_password(cd['password']),email=cd['email'],siteurl=cd['url'])
                return  render(request,'success.html',{})
            else:
                return render(request,'failure.html',{})
        else:
            reg_form = RegForm()
    except:
        print 'cuole'
    return render(request,'reg.html',locals())

def login(request):
    print request.get_host()
    errors=[]
    if request.method == 'POST':
        username =request.POST.get('username','')
        password = request.POST.get('password','')
        if not request.POST.get('username',''):
            errors.append('enter a username')
        if not request.POST.get('password',''):
            errors.append('enter a password')
        if not errors:
            if not request.user.is_authenticated():
                user = auth.authenticate(username=username,password=password)
                if user is not None and user.is_active:
                    auth.login(request,user)
                    return  HttpResponseRedirect(request.POST.get('source_url'))
                else:
                    return HttpResponse('username or password invalid.')
            else:
                return HttpResponseRedirect('/')
    return render(request,'login.html',locals())

def archive(request):
    try:
        # 获取客户端的信息
        year = request.GET.get('year', None)
        month = request.GET.get('month', None)
        archives = Article.objects.distinct_date()
        article_list = Article.objects.filter(date_publish__icontains = year+'-'+month)
        print article_list
        article_list = pag(request, article_list)
    except Exception as e:
        print e

    return render(request, 'archive.html', locals())

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/login/')

@login_required(login_url = '/login/')
def write_article(request):
    if request.method=='POST':
        print 'YES'
    else:
        form = Write_articleForm()
    return render(request,'write_article.html',locals())
