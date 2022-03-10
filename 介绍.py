#manage  表示的是一个命令行工具,可以让使用多种方式来进行Django进行交互
#init  表示的是一个控件,告诉Python此目录应该被看成一个Python包
#setting 表示的是项目的配置文件
#urls  表示的是项目的URL声明
#wsgi  是项目与wsgi兼容的web服务器入口

#如果出现问题,将数据库整个删掉,将迁移文件也删掉

"""
基本操作:
1.数据库里面设计表结构,比如班级表结构(表名,字段:时间.学生整数.是否删除)和学生表结构
2.配置数据库,注意Django默认使用的是SQLite数据库,要是想使用MySQL需要在setting.py中通过database选项来进行配置MYSql
    首先在initpy里面输入import pymysql
                    pymysql.install_as_MySQLdb()
    之后在setting里面配置,将SQLite改成mysql
3.创建应用
在一个项目中可以创建多个应用,每个应用进行一种业务处理
就可以直接创建一个项目,比如APP1admin表示额是站点配置
4.激活应用
在setting.py文件中,将APP1加入到installed_apps选项中,pycharm里面已经创建
5.定义模型
  概述:一个数据表对应一个模型,在models.py文件里面定义模型
6.在数据库中生成数据表
   生成迁移文件  就是migrations
   生成迁移 终端执行
   cd /Users/zan/djangoProject
   python manage.py makemigrations
   但是此时数据库还没有表
   终端执行python manage.py migrate
   上面的相当于执行MySQL语句来创建数据表
7.测试数据操作
  进入终端执行
  cd /Users/zan/djangoProject
  python manage.py shell
  引入包from app1.models import Grades,Students
        from django.utils import timezone
        from datetime import *
 查询所有数据Grades.objects.all()  //类名.objects.all()
 添加数据:本质就是创建一个模型类的对象实例
     grade1=Grades()
     grade1.gname="Ana"
     grade1.gdate=datetime(year=2021,month=11,day=27)
     grade1.ggnum=2
     grade1.gbnum=2
     grade1.save()  //将数据存到数据库里面
 查看某个对象
    Grades.objects.get(pk=1)
 修改数目
    grade1.ggnum=40
    grade1.save()
 删除
     grade1.delete()  注意数据库里面表的数据也删除
 形成外键的时候
    grade2=Students()
    grade2.sgrade=grade1  //此处表示的就是线程一个外键,此时就关联一个对象
 获取关联对象的集合
    对象名.关联的类名小写_set.all()  grade1.students_set.all()

 启动服务器
 格式:cd /Users/zan/djangoProject python manage.py runserver ip:port
    在浏览器输入127.0.0.1:8000/
    ip可以不写 上面的是一个纯Python写的轻量级web服务器,仅仅在开发测试时候使用

 admin站点管理
   概述:内容发布包含了添加,修改,删除内容
   配置admin应用,在settings里面配置在installedAPP里面添加'django.contrib.admin'  此时默认是已经添加成功
   创建管理员用户cd /Users/zan/djangoProject python manage.py createsuperuser  zan 182515131
   之后再上面的web页面8000后面加上admin
   汉化:修改settings language_code="zh-Hans'  time_zone='Asia/Shanghai'

 管理数据表
    修改admin.py文件

    from .models import Grades,Students
    #注册表
    admin.site.register(Grades)
    admin.site.register(Students)
    自定义管理页面

    #列表页属性
    list_display = []
    list_filter = []
    search_fields = []
    list_per_page = []

    关联对象
    需求:在创建一个班级的时候,可以直接添加几个学生
    bool值显示问题,可以定义一个函数
"""

"""
视图的基本使用:
   概述:视图表示的是对web的请求进行相应,视图就是一个Python函数,在views里面定义
     修改project文件下urls文件
     在app1里面创建urls文件
     
"""

"""
模板的基本使用:
    模板是HTML页面,根据视图中传递过来的数据来填充,将数据渲染
    创建模板,就是templates,再在目录下面,创建文件夹对应项目
    配置路径,就是修改settings.py文件,其中settings里边的basicdir就是project文件路径,因此修改下面的template的dirs的时候,直接使用
    os.path.join(BSAE_DIR,'templates'),但是pycharm创建的时候自动创建了
    要想在页面上直接显示班级,需要定义模板,在app1下面创建grades.html以及students.html
    模板语法:接下来可以在students以及grade的HTML中查看
    接下来要继续增发url因此需要在项目的url增发url里面配置好班级的视图html之后,再去视图里面修改,之后在视图里面去模板中取数据,将其作为一个列表,然后再将数据传递给模板,grades里面所做的修改表示的就是渲染
"""

