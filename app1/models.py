from django.db import models

# Create your models here.
#定义好了一个模型类
class Grades(models.Model):
    gname=models.CharField(max_length=20)
    gdate=models.DateField()
    ggnum=models.IntegerField()
    gbnum=models.IntegerField()
    isDelete=models.BooleanField(default=False)
    def __str__(self):
        return self.gname
    class Meta:
        db_table="grades"
        ordering=[]

class studentsManager(models.Manager):
    def get_query(self):
        return super(studentsManager,self).get_queryset().filter(isDelete=False)  #过滤前面表示的是原始的数据,但是过滤后面就是加上了条件限制
#在管理器中添加对象
    def createStudent(self,name,age,gender,contend,grade,lastT,createT,isD=False):
        stu=self.model()
        stu.sname = name
        stu.sage = age
        stu.sgender = gender
        stu.scontend = contend
        stu.sgrade = grade
        stu.lastTime=lastT
        stu.createTime=createT
        return  stu


class Students(models.Model):
    stuObj=models.Manager()  #表示的是自定义管理器,当自定义模型管理器的时候,object就不存在了
    stuObj1=studentsManager()
    sname=models.CharField(max_length=20)
    sgender=models.BooleanField(default=True)
    sage=models.IntegerField(db_column='age')
    scontend = models.CharField(max_length=20)
    isDelete = models.BooleanField(default=False)
    #对应班级的时候出现了一对多的现象,所以要找一个主键,此时要关联一个外键
    sgrade=models.ForeignKey("Grades",on_delete=models.CASCADE)
    #但是数据库里面没有表
    def __str__(self):
        return self.sname

    lastTime = models.DateTimeField(auto_now=True)
    createTime = models.DateTimeField(auto_now=True)

    class Meta:
        db_table="students"
        ordering=['-id']

    #定义一个类方法创建对象
    @classmethod  #此处表示下面的方法就是类方法
    def createStudent(cls,name,age,gender,contend,grade,lastT,createT,isD=False):  #cls代表就是students那个类
        stu=cls(sname=name,sage=age,sgender=gender,scontend=contend,sgrade=grade,lastTime=lastT,createTime=createT,isDelete=isD)
        return stu   #将创建的对象返回

    #创建一个方法
    def getName(self):
        return self.sname

class TempTables(models.Model):
    a=models.BooleanField(default=True)  #这里表示的是可以增加表以及增加迁移文件




