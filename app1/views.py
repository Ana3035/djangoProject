

from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from django.db.models import Max, F, Q
from django.contrib.auth import logout

# Create your views here.
# 定义视图
from app1.models import Grades, Students


def index(request) :  # 表示的是请求体
    return HttpResponse("Ana")


def detail(request, num, num2) :  # 表示接受数字
    return HttpResponse("detail-%s-%s" % (num, num2))


def grades(request) :
    # 去模板里面取数据
    gradesList = Grades.objects.all()  # 取出来了班级列表
    # 将数据传递给模板,模板渲染页面,将渲染好的页面传递给浏览器 grades表示的就是模板里面的对象
    return render(request, 'app1/grades.html', {'grades' : gradesList})


def grades1(request) :
    # 表示的是F对象
    f = Grades.objects.filter(ggnum__gt=F('gbnum') + 5)
    # 表示的是Q对象,注意只有一个Q对象的时候就是直接匹配,没有或者的意思,只有一个的时候前面加上~表示的是取反
    q = Students.stuObj1.filter(Q(pk__lte=3) | Q(sage__gt=20))
    q1 = Students.stuObj1.filter(~Q(pk__lte=3))
    print(f, q, q1)
    return HttpResponse("XXXX")


def students(request) :
    studentsList = Students.stuObj1.all()
    return render(request, 'app1/students.html', {'students' : studentsList})


# 显示前1个学生
def students1(request) :
    studentsList = Students.stuObj1.all()[0 :1]
    return render(request, 'app1/students.html', {'students' : studentsList})


# 分页显示学生
def stuPage(request, page) :
    # 0-5 5-10 10-15
    page = int(page)
    studentsList = Students.stuObj1.all()[(page - 1) * 5 :(page) * 5]
    return render(request, 'app1/students.html', {'students' : studentsList})


def studentsearch(request) :
    studentsList = Students.stuObj1.filter(sname__contains="康")
    return render(request, 'app1/students.html', {'students' : studentsList})


def studentstaend(request) :
    studentsList = Students.stuObj1.filter(sname__startswith="赵")
    studentsList1 = Students.stuObj1.filter(sname__endswith="羽")
    studentsList2 = Students.stuObj1.filter(pk__in=[1, 2])
    studentsList3 = Students.stuObj1.filter(sage__gt=22)
    studentsList4 = Students.stuObj1.filter(lastTime__day=30)
    # 此处表示的是描述中带有赵安南的班级
    grades5 = Grades.objects.filter(students__scontend__contains="霍薪羽")
    print(grades5)
    MaxAge = Students.stuObj1.aggregate(Max("sage"))  # 注意上面需要引入包

    print(MaxAge)  # 取出的是最大的值

    return render(request, 'app1/students.html', {'students' : studentsList4})


def gradesStudents(request, num) :
    grade = Grades.objects.get(pk=num)  # 表示的是将班级下面所有的学生都取出来了,pk表示的是对应的班级
    studentsList = grade.students_set.all()
    return render(request, 'app1/students.html', {'students' : studentsList})


def addstudent(request) :
    grade = Grades.objects.get(pk=1)
    stu = Students.createStudent("霍老炮", 25, True, "请多指教", grade, "2021-8-8", "2021-5-5")
    stu.save()
    return HttpResponse("ok")


def addstudent2(request) :
    grade = Grades.objects.get(pk=1)
    stu = Students.stuObj1.createStudent("康康", 25, True, "请多指教", grade, "2021-8-8", "2021-5-5")
    stu.save()


#########################
def attribles(request) :
    print(request.path)
    print(request.method)
    print(request.GET)
    print(request.POST)
    print(request.FILES)
    print(request.COOKIES)
    print(request.session)
    return HttpResponse("今天也要加油鸭")


# 获取get传递的数据
def get1(request) :
    a = request.GET.get('a')
    b = request.GET.get('b')
    c = request.GET.get('c')
    return HttpResponse(a + " " + b + " " + c)


def get2(request) :
    a = request.GET.getlist('a')  # 注意这里是一个列表
    a1 = a[0]
    a2 = a[1]
    b = request.GET.get('b')
    return HttpResponse(a1 + " " + a2 + " " + b)


#######################

# 获取post传递过来的数据
def showregister(request) :
    return render(request, 'app1/register.html')


def register(request) :
    name = request.POST.get("name")  # 就是键值属性
    sex = request.POST.get("sex")
    age = request.POST.get("age")
    hobby = request.POST.getlist("hobby")
    print(name)
    print(sex)
    print(age)
    print(hobby)
    return HttpResponse("post")


# 修改project的urls文件

##########
def showresponce(request) :
    res = HttpResponse()
    res.content='Ana'
    print(res.content)
    print(res.charset)
    print(res.status_code)
    print(res.content-type)
    return res

###################
#cookie
def cookietest(request):
    res=HttpResponse()
    cookie=request.COOKIES  #此时就是读取下面上一次已经存入的cookie
    res.write("<h1>"+cookie["Ana"]+"</h1>")  #此时显示出来的就是下面上一次存入的值
    #cookie=res.set_cookie("Ana","good")#此时数据就已经存入
    return res

#重定向
#想实现的是执行下面的1的页面的时候,跳转到2的页面上
def redirect1(request):
    #return HttpResponseRedirect('/redirect2')
# 编写redirect函数
    return redirect('/Ana/redirect2')  #这个相比较下面的更加灵活,且可以使用正则表达式
def redirect2(request):
    return HttpResponse("我是重定向之后的视图")
def redirect3(request):
    if request.is_ajax():
        a=JsonResponse({})
        return a

#########################
# session
#显示登录界面
def main(request):
    #取出下面存储的session
    #usrname='游客'
    usrname=request.session.get('name','游客')#后面的表示的是如果没取到就是后面的游客的值
    return render(request,"app1/main.html",{'usrname':usrname})

def login(request):
    return render(request,"app1/login.html")

def showmain(request):
    #将session存储起来
    usrname=request.POST.get('usrname')  #表示的是点击页面响应一个post请求之后将post的值拿出来
    #存储session
    request.session['name']=usrname
    request.session.set_expiry(5)#设置5秒之后过期
    return redirect('/Ana/main')  #表示的 是重定向

def quit(request):
    #清除session
    logout(request)
    return redirect('/Ana/main')



###############################################
#模板部分
def indexM(request):
    #传递参数
    student=Students.stuObj1.get(pk=1)
    return render(request, 'app1/temp.html',{"stu":student,'num':10,'str':"good good study",'list':["a","b",'c'],'text':30,'code':'<h1>der</h1>'},)
    #传递数字
    #return render(request,'app1/temp.html',{'num':10})
    #传递列表
    #stuList=Students.stuObj1.all()
    #return render(request,'app1/temp.html',{'stus':stuList})

#反向解析
def good(request,id,ig):
    return render(request,'app1/good.html',{'num':id},{'nu':ig})

#继承
def main1(request):
    return render(request, 'app1/main1.html')

def detail1(request):
    return render(request, 'app1/detail.html')


