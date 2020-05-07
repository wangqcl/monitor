from django.db import models
from datetime import datetime

#用户信息模型
class Users(models.Model):
    username = models.CharField(max_length=32) #账号
    name = models.CharField(max_length=16)      #真实姓名
    password = models.CharField(max_length=32)  #密码
    sex = models.IntegerField(default=1)        #性别
    phone = models.CharField(max_length=16)     #电话
    email = models.CharField(max_length=50)     #Emai
    state = models.IntegerField(default=1)      #状态
    comp_id = models.IntegerField()             #对应公司信息ID
    addtime = models.DateTimeField(default=datetime.now)    #注册时间

    def toDict(self):
        return {'id':self.id,'username':self.username,'name':self.name,'password':self.password,'phone':self.phone,'email':self.email,'state':self.state,'comp_id':self.comp_id,'addtime':self.addtime}

    class Meta:
        db_table = "users"  # 更改表名

#公司信息表
class Compinfo(models.Model):
    comp_name = models.CharField(max_length=16)  # 企业名称
    address = models.CharField(max_length=255)  # 地址
    name = models.CharField(max_length=16)  # 企业联系人
    phone = models.CharField(max_length=16)  # 电话
    comp_ip = models.CharField(max_length=32)  # 企业IP
    comp_realm = models.CharField(max_length=32)  # 企业域名
    addtime = models.DateTimeField(default=datetime.now)  # 注册时间

    def toDict(self):
        return {'id':self.id,'comp_name':self.comp_name,'address':self.address,'name':self.name,'phone':self.phone,'comp_ip':self.comp_ip,'comp_realm':self.comp_realm,'addtime':self.addtime}

    class Meta:
        db_table = "compinfo"  # 更改表名