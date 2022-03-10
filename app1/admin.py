from django.contrib import admin

# Register your models here.
from .models import Grades,Students

#注册表
class StudentTnfo(admin.TabularInline):  #表示的是创建一个班级的时候获得两个学生
    model = Students
    extra = 2
class GradeAdmin(admin.ModelAdmin):
    #列表页属性
    inlines = [StudentTnfo]  #此时在grades页面就会显示出来两个空行可以填写信息
    list_display = ['pk','gname','gdate','ggnum','gbnum','isDelete']  #显示字段
    list_filter = ['gname']  #就是一个过滤条件,过滤字段
    search_fields = ['gname']  #定义了查找条件
    list_per_page = 5  #表示的是每个五条分页

    # #添加修改页属性
    #fields = ['ggnum','gbnum','gname','gdate']  #在右上角显示出来的,点击进去就可以看到修改了顺序
    fieldsets = [
        ('num',{"fields":['ggnum','gbnum']}),
        ("base",{"fields":['gname','gdate','isDelete']}),
    ] #点击到1那里就可以直接修改了,表示的是给属性分组,但是要注意的是和上面不能同时使用
admin.site.register(Grades,GradeAdmin)  #注意这里要加上上面的类

@admin.register(Students)  #表示的是装饰器
class StudentAdmin(admin.ModelAdmin):
    def __init__(self, model, admin_site) :
        super().__init__(model, admin_site)
        self.sgender = None

    def gender(self):
        if self.sgender:
            return '男'
        else:
            return '女'
    #设置页面列的名称
    gender.short_description="性别"
    list_display = ['pk','sname','sage','scontend',gender,'sgrade','isDelete']
    list_per_page = 2
    #执行动作的位置
    actions_on_bottom = True
    actions_on_top = False
    #当使用装饰器完成注册的时候下面这句话就不要写
# admin.site.register(Students,StudentAdmin)
