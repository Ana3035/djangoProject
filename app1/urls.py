from django.urls import path, re_path
from . import views  # 表示的是在当前目录下引入views

urlpatterns = [
    path('', views.index),
    re_path(r'(\d+)/(\d+)', views.detail),  # 中间的正则表示的一个组
    path('grades/', views.grades),
    path('grades1/', views.grades1),
    path('students/', views.students),
    path('students1/', views.students1),
    path('studentsearch/', views.studentsearch),
    path('staend/', views.studentstaend),
    re_path(r'stu/(\d+)/', views.stuPage),
    re_path(r'grades/(\d+)', views.gradesStudents),
    re_path('addstudent/', views.addstudent),
    re_path('addstudent2/', views.addstudent2),
    path('attribles/', views.attribles),
    path('get1/', views.get1, ),
    path('get2/', views.get2, ),
    path('showregister/', views.showregister, ),
    path('showregister/register/', views.register, ),
    path('showresponce/', views.showresponce, ),
    path('cookietest/', views.cookietest),
    path('redirect1/', views.redirect1),
    path('redirect2/', views.redirect2),
    path('main/', views.main),
    path('login/', views.login),
    path('showmain/', views.showmain),
    path('quit/', views.quit),
    path('temp/', views.indexM),
    # 下面的表示的是可以动态生成需要匹配的网址

    re_path(r'good/(\d+)/(\d+)/', views.good,name="good"),

    path('main1/',views.main1),
    path('detail/',views.detail1)

]
