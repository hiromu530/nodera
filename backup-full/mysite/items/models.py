from django.db import models
from django.utils import timezone

# Create your models here.

class Items(models.Model):
    
    class Meta(object):
        
        db_table = 'items'
        
    text = models.CharField(verbose_name = '本文',max_length=255)
    created_at = models.DateTimeField(verbose_name='作成時刻',help_text ='作成時刻',default=timezone.now)
    topictitle = models.CharField(verbose_name = 'トピックタイトル',max_length=20,default='トピックタイトル')
    itemid = models.CharField(verbose_name='id',max_length=10,default='0')
    user = models.CharField(verbose_name='user',max_length=255,default='ユーザーネーム')
    
    def __str__(self):
        return self.text,self.created_at,self.topictitle,self.itemid
    
class  Topics(models.Model):
    class Meta(object):
        db_table = 'topics'
        
    title = models.CharField(verbose_name='トピックタイトル',max_length=20)
    created = models.DateTimeField(verbose_name='更新日時',help_text='更新日時',default=timezone.now)
    posts = Items
    user = models.CharField(verbose_name='user',max_length=255,default='ユーザーネーム')
    
    def __str__(self):
        return self.title,self.created,self.posts
    
class Users(models.Model):
    class Meta(object):
        db_table = 'users'
        
    username = models.CharField(verbose_name='user',max_length=255,default='ユーザーネーム')
    passward = models.CharField(verbose_name='pass',max_length=6,default='パスワード')
    
    def __str__(self):
        return self.username,self.passward