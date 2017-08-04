# coding=utf-8
from django import forms
from blog.models import *
class RegForm(forms.Form):
    username = forms.CharField(widget = forms.TextInput(attrs={"placeholder":"username","required":"required"}),max_length=50)
    password = forms.CharField(widget = forms.PasswordInput(attrs={"placeholder":"password","required":"required"}),max_length=20)
    email = forms.EmailField(widget = forms.TextInput(attrs={"placeholder":"email","required":"required"}),max_length=50)
    url = forms.CharField(widget = forms.URLInput(attrs={"placeholder":"url","required":"required"}),max_length=50)

class CommentForm(forms.Form):
    author = forms.CharField(widget=forms.TextInput(attrs={"placeholder":"author","required":"required"}),max_length=50,error_messages={"required":"username不能为空",})
    email = forms.EmailField(widget=forms.TextInput(attrs={"placeholder":"email","required":"required"}), max_length=50, error_messages={"required":"email不能为空",})
    url = forms.URLField(widget=forms.TextInput(attrs={"placeholder":"url","required":"required"}),max_length=100, required=False)
    comment = forms.CharField(widget=forms.Textarea(attrs={"placeholder":"comment","required":"required"}),error_messages={"required":"评论不能为空",})

class Write_articleForm(forms.ModelForm):
    # category_id = Article.objects.get('category')
    # category = category_id.category.name
    # tag = Article.objects.get('tag')
    # title = forms.CharField(widget = forms.TextInput(attrs={"placeholder":"title","required":"required"}),max_length =50,label='标题')
    # desc = forms.CharField(widget = forms.TextInput(attrs={"placeholder":"desc","required":"required"}),max_length =100,label='描述')
    # click_count = forms.IntegerField(widget = forms.NumberInput(attrs={"placeholder":"click_count","required":"required"}),label='点击量')
    # is_recommend = forms.BooleanField(widget = forms.NullBooleanSelect(attrs={"placeholder":"is_recommend","required":"required"}),label='推荐')
    # content = forms.CharField(widget = forms.Textarea(attrs={"placeholder":"comment","required":"required",'cols': 0 , 'rows': 0}),label='文章内容')
    # # category = forms.ChoiceField(choices = category)
    # tag = forms.ChoiceField(widget = forms.SelectMultiple(attrs=tag))
    # class Meta:
    #     widgets = {
    #     'name' : Textarea(attrs={'cols': null , 'rows': null}),
    #     }
    class Meta:
        model = Article
        fields = '__all__'
        labels = {
            'title':'标题',
            'desc':'描述',
            'content':'文章',
            'is_recommend':'推荐',
            'click_count': '点击',
            'category': '分类',
            'tag': '标签',
            'user': '作者'
        }
