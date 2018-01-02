from viewInfo.mongodbInfo import account
from mongoengine import *
# Create your models here.

#这里使用了我的服务器
#账户密码并未上传至git
ac=account()
connect(ac.db, host=ac.host, port=27017 , username=ac.user, password=ac.password)

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
    meta = { 'collection': ac.collection} # 指明连接数据库的哪张表
