# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class ArticleManager(models.Manager):
    def distinct_date(self):
        distinct_date_list = []
        date_list = self.values('date_publish')
        for date in date_list:
            date = date['date_publish'].strftime("%Y/%m") + "文章归档"
            if date not in distinct_date_list:
                distinct_date_list.append(date)
        return distinct_date_list

class Category(models.Model):
    name = models.CharField(max_length = 20)
    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name

class Site(models.Model):
    name = models.CharField(max_length = 20)
    desc = models.CharField(max_length = 100)
    def __unicode__(self):
        return self.name
    class Meta:
        verbose_name = '标题'
        verbose_name_plural = verbose_name

class Tag(models.Model):
    name = models.CharField(max_length = 20)
    def __unicode__(self):
        return self.name
    class Meta:
        db_table = 'tag'
        verbose_name = '标签'
        verbose_name_plural = verbose_name
class User(AbstractUser):
    siteurl = models.URLField(blank = True,null = True,verbose_name = '网址')
    avatar = models.ImageField(upload_to = 'avatar/%Y/%m',default = 'avatar/default.jpg',max_length = 200,null = True,verbose_name = '用户头像')
    class Meta:
        verbose_name = '用户'
        verbose_name_plural = verbose_name
    def __unicode__(self):
        return self.username

class Article(models.Model):
    title = models.CharField(max_length = 50)
    date_publish = models.DateTimeField(auto_now_add = True)
    content = models.TextField(null = True ,blank = True)
    desc = models.CharField(max_length = 100 ,null = True)
    click_count = models.IntegerField(null = True)
    is_recommend = models.BooleanField(default = False, verbose_name = '是否推荐')
    category = models.ForeignKey(Category)
    tag = models.ManyToManyField(Tag)
    user = models.ForeignKey(User)
    objects = ArticleManager()
    def __unicode__(self):
        return self.title
    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name
        ordering = ['-date_publish']



class Ad(models.Model):
    callback_url = models.URLField(null = True,blank = True)
    image_url = models.ImageField(upload_to = '%Y/%m' )
    description = models.CharField(max_length = 20,blank = True,null = True)
    def __unicode____(self):
        return '首页大图'
    class Meta:
        verbose_name = '首页大图'
        verbose_name_plural = verbose_name

class Link(models.Model):
    title = models.CharField(max_length = 20)
    callback_url = models.URLField()
    def __unicode__(self):
        return self.title
    class Meta:
        verbose_name = '友链'
        verbose_name_plural = verbose_name

class Comment(models.Model):
    user = models.ForeignKey(User,null = True,blank =True)
    username = models.CharField(max_length = 30,blank = True,null=True)
    email = models.EmailField(max_length=50,blank=True,null=True)
    url = models.URLField(max_length = 100,blank=True,null=True)
    article = models.ForeignKey(Article)
    date_publish = models.DateTimeField(auto_now_add = True)
    content = models.TextField()
    pid = models.ForeignKey('self',blank = True,null = True)
    def __unicode__(self):
        return self.content
    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name
