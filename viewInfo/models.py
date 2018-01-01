from django.db import models
from mongoengine import *
# Create your models here.
connect('qzrc', host='139.199.159.233', port=27017 , username='abfahrt', password='abfahrt')

class Info(Document):
    url = StringField()
    userName = StringField()
    foreignFirst= ListField(StringField())
    workExps= ListField(StringField())
    nativePlace= StringField()
    graduationTime= StringField()
    hopeSalary= StringField()
    politicsStatus= StringField()
    qq= StringField()
    selfAssessment= StringField()
    workExperience= StringField()
    hopeLocation= StringField()
    telNumber= StringField()
    jobHunt= StringField()
    nowLocation= StringField()
    highestEducation= StringField()
    sex= StringField()
    address= StringField()
    workType= StringField()
    birth= StringField()
    foreignSecond= ListField(StringField())
    education= ListField(StringField())
    huntType= StringField()
    weight= StringField()
    height= StringField()
    idCardNumber= StringField()
    employmentCategory= StringField()
    maritalStatus= StringField()
    major= StringField()
    email= StringField()
    meta = { 'collection': 'infos'} # 指明连接数据库的哪张表

for i in Info.objects[:10]: # 测试是否连接成功
    print(i.education[0])