"""
url首先接收到信息,url匹配到对应的视图,将视图交给模板,模板再渲染,传递给视图,视图再传递给浏览器
视图作用:视图接受web请求,且响应web请求,url只执行分配的功能,响应的功能是视图来做的
    本质:就是一个Python中的函数,在views俩面呈现出来的就是函数
    响应:网页:
            重定向:
            错误视图:404表示的是网址没有走通 500表示的是服务器内部错误
        json数据
    响应过程:1.用户在浏览器输入网址 2.Django获取到了网址的信息,且取出IP端口,  3.交给URL管理器,诸葛匹配URL配置,成功之后,执行对应的视图函数  4.将函数名交给视图管理器,其实就是找到对应的函数,执行的结果就是返回结果给浏览器

"""

"""
URL配置流程:
    指定根级url配置文件,就是在settings里面的root里面配置的就是ROOT_URLCONF = 'djangoProject.urls',默认已经实现
    在Django项目俩面的url的传递的第一个是正则表达式,第二个就是函数名称
    匹配正则的注意事项:
        1.需要加上小括号 2.前面不需要含有斜杠 3.但是在匹配的后面需要加上斜杆
    
引入其他url配置,因为可能有不同的项目,所以直接在不同的项目上面创建自己的url配置,在工程url中引入APP1的url

url的反向解析,如果在页面中修改了正则表达式,那么接下来都要修改,此时工作量会非常大,在url配置发生改变的时候,多态生成链接的地址就能解决上述的问题,表示的就是视图俩面的链接自动修改
    解决思路:在使用链接的时候,通过url的配置的名称,动态生成url的地址
    作用:在使用url模板的时候
    
"""

"""
视图函数:
    定义视图:本质上就是一个函数
        视图参数:一个HttpRequest实例,通过正则表达式来获取的参数,在views里面定义
    错误视图:404视图:在找不到网页的时候返回的视图,就是url匹配不成功返回的视图
                    此视图可以自己定义,在template目录下面可以自己定义404.html,自己写出一个页面网址
                    配置settings.py
                        DEBUG = True  如果是true那永远不会调用404页面,所有应该是False
                        ALLOWED_HOSTS = [] 里面加上'*'
            500视图:表示的是在视图代码中出现错误,就是服务器本身错误
            400视图:错误出现在客户的操作,比如说服务器发现可能是爬虫
"""

"""
    两个对象:
        HttpRequest:表示的其实就是request对象,
            概述:服务器接收http请求之后,会根据报文创建httprequest对象,视图的第一个参数就是httprequest对象,其中request表示的是形参,是Django创建的,创建之后调用视图的时候,会传递给视图
            属性:针对的是request对象来说的,
                path:表示请求的完整路径,但是不包括域名以及端口
                method表示请求的方式,常用的有get和post
                encoding表示浏览器提交数据的编码方式
                GET表示的是类似字典的对象,包含了get请求的所有参数就是后面类似于?3%5之类的东西
                POST也类似于上面,就是类似字典的对象
                FILES表示的也是类似于字典的对象,包含了所有上传的文件
                COOKIES就是一个字典,包含了所有的cookie
                session也是类似于字典的对象,表示当前会话
                
            方法:is_ajax()如果是通过XMLHttpRequest发起的则返回的是True,因为ajax请求返回的一般是Jason数据
            
            QueryDict对象:request对象里面的GET和POST对象都属于QueryDict对象
                    方法:get:可以根据建获取值,只可以返回一个值
                        getlist:将键的值以列表的形式返回,可以返回多个值,比如后面的含有两个a=
                        
            
            GET属性:http://127.0.0.1:8000/Ana/get1?a=1&b=2&c=3
                    http://127.0.0.1:8000/Ana/get2?a=1&a=2&c=3
                    上述的作用是获取浏览器传递过来的数据
            
            POST属性:使用表单实现post请求
            CSRF verification failed. Request aborted.页面出现如上报错的时候,去settings里面修改关闭csrf
            
        HttpResponse对象:作用:表示的是给浏览器返回数据,HttpRequest对象是由Django创建的,而HttpResponse对象是由程序员创建的
            用法:不调用模板,直接返回数据,就是指的是直接return response
                调用模板:直接使用render方法
                        原型:render(request,templateName[content])
                        作用:结合数据和模板返回一个HTML的页面
                        参数:第一个是请求体对象,第二个是模板路径,第三个是传递给需要渲染在模板上面的数据
                        实例:def showregister(request):
                                        return render(request,'app1/register.html')
                                        
            属性:content表示的是返回内容的类型
                charset表示返回数据的编码格式
                status_code表示响应的状态码
                content-type指定输出的mime类型
                
            方法:
                init使用页面内容实例化Httpresponce对象
                write(content)表示的是以文件的形式输出缓冲区
                flush()以文件的形式输出缓冲区
                set_cookie(key,value='',max_age=None,exprise=None)表示的是设置主体
                delete_cookie表示的是删除主体
                浏览器登录发给服务器一些信息,服务器验证,去Redis里面查找,如果Redis没有,那么去数据库里面查找,
            
            子类HttpResponseRedirect:
                功能:表示的是重定向,显示的是服务器的跳转
                简写:redirect(to)
            
            子类JsonResponse
                返回JSON数据,一般用于异步请求(ajax)
                创建:__init__(self.data)其中data就是一个字典的对象
                注意:content-type类型是application/json类型
                
"""

"""
状态保持:
    概述:http协议是无状态的,每次请求都是一次新的请求,不记得以前的请求页面1显示的是登录的页面,如果想要记住,那么则表示的是一种状态的保持,客户端和服务器的一次通信就是一次会话,要想实现状态的保持,那么就要在客户端或者服务器存储有关会话的数据.
        存储的方式:session(所有的数据都存在服务端,在客户端用cookie存储session_id),cookie(所有的数据都存储在了客户端,但是不要存储敏感的数据)
        状态保持的目的:在一段事件内跟踪请求者的状态,可以实现跨页面访问当前请求者的数据
        注意,不同的请求者之间不会共享这个数据,与请求者之间是一一对应的
    
    启用session,在settings文件里面默认是请求的,
    使用session后:每个httprequest对象都有一个session属性,就是一个类似字典的对象
        get(key,default=None)表示的是根据键获取session的值
        clear()表示的是清空所有的会话
        flash()删除当前的会哈,且删除会话的cookie
    
    首先有一个欢迎页面,点击登录按钮,跳转到登录的界面,登录完之后再跳转回来,此时显示的就是用户名的界面
    
    设置过期时间:set_expiry(value) 如果不设置,两个星期之后过期,如果是10表示的就是10秒之后过期
                0  表示的是关闭浏览器的时候失效
                None表示的是永不过期
                
    存储session的位置:
                数据库:默认存储在数据库里面
                缓存:只存储在本地,如果丢失不能找回,比数据库要快
                数据库和缓存:优先从本地缓存里面读取,读取不到再去数据库里面获取
                
    使用redis
"""