"""
一、基本命令
1、连接mysql:PATH="$PATH":/usr/local/mysql/bin
          mysql -u root -p
          182515131
2、查看版本类型：select version();  此时注意一定要加上分号
3、查看当前时间：select now();
4、远程连接
    格式：mysql -h ip地址 -u 用户名 -p
    输入对方的数据库密码

二、数据库操作的命令
1、创建数据库
create database 数据库名称 charset=utf8;
2、删除数据库
drop database 数据库名称 ;
3、切换数据库
use 数据库名称；
4、查看当前数据库
select database；

三、表操作的命令
1、查看当前数据库里面含有哪些表
show tables;
2、创建表
create table student(id int auto_increment primary key,name varchar(20) not null);  那个单词表示的是自增长
3、删除表
drop table 表名；
4、查看表结构(以后注意不能轻易修改表的结构，因为数据可能出现错误，所以一开始的时候，最好预留出行
desc 表名 ;
5、查看建表语句
show create table 表名;
6、重命名表
rename table 源表名 to 新表名;
7、修改表
alter table 表名 add|change|drop 列名 类型

四、数据操作的命令（增删改查）
1、增加数据
  a、全列插入：insert into 表名 values(所存的数值)   #主键列是自动增长的，但是在全列插入的时候需要占位，通常使用的是0，插入成功之后以实际的数据为准,这里要注意的是所存的数据值要按照列的名称对应的数据类型来存取
  b、缺省插入：insert into 表名（列1，列2） values(值1，值2）   #注意主键列通常不需要缺省，因为是自动生成数据，不会有缺省值
  c、同时插入多条数据：insert into 表名 values（。。。）,（。。。）;

2、删
delete from 表名;这个表示的是全部删除
delete from 表名 where 条件（比如id=4）;

3、改
update 表名 set 列1=值1，..... where 条件；   没有条件的表示的是全部修改
update student set isdelete=0 where id=2;
4、查
select * from 表名   #表示的是查询表中的全部数据

五、查
1、基本语法
select * from 表名  #表示的是数据来源这张表，*号表示的是集中显示表中的所有列，但是也可以直接加上列名
select column as newname from 表名  #此时表示的是为列起一个别名，且这个别名显示在结果集中
如果查询多个列，中间用逗号分割：select id,name from student;
                           select id as a,name from student;  表示的就是上面的别名
2、消除重复行
在select后面列的前面使用distinct就可以消除重复行
select distinct isdelete from student  结果就不会显示重复的行
3、条件查询
   a、语法
   select * from 表名 where 条件
   b、比较运算符
    = > < >= <= !=或者<>
    select id from student where id>8;
   c、逻辑运算符
   and or not
   select * from student where id>1 and isdelete=0;
   d、模糊查询
    like   %表示任意多个任意字符  _表示一个任意字符
    select * from student where name like "赵%"  相当于正则表达式
    select * from student where name like "赵_"
   e、 范围查询
   in 表示在一个非连续的范围内
   between   and  表示的在一个连续的范围内

   select * from student where id in (8,10,12);
   select * from student where id between 4 and 8;
   f、空判断
   null 和 ""是不同的  后面的是一个字符串数据，但是前面的就是没有数据
   is null   &  is nou null
   select * from student where address is null;
   g、优先级
   小括号，not ，比较运算符，逻辑运算符  and比or的优先级高
4、聚合
为了快速得到统计数据，提供了五个聚合函数
    count(*)   表示计算总行数，*也可以是列名
    max(列) min(列)   表示求这个列的最大值最小值
    sum(列)   求和
    avg(列)   求平均值

    select count(*) from student;
    select max(id) from student where gender=0;
5、分组
按照字段分组，表示此字段相同的数据会被放到一个集合中；分组后只能查询查询相同的数据列，对于有差异的数据列无法显示在结果集中，
之后可以对分组后的数据进行统计，做聚合运算
select 列1，列2...，聚合----from 表名 group by 列1....   #by后面的表示
查询男女生总数
select gender,count(*) from student by gender

分组后进行数据的筛选：
select 列1，列2...，聚合----from 表名 group by 列1....，having 列1....，聚合-----
select gender age,count(*) from student by gender  having age>20
#having表示的是从结果集里面筛选数据

where  & having的区别，第一个是对from后面指定的表进行筛选，但是后面的一个表示的是对结果进行筛选
6、排序
select # from 表名 order by 列1 asc|desc 列2,asc|desc 列3   #前面的是升序，后面的是将序
将数据按照列1进行排序，如果某些列1 的值相同，则按照列2进行排序
默认按照从小到大的顺序排序
7、分页
select # from 表名 limit start ,count;   后面的是哪个参数必须要给值
select # from student limit 0,3;   #表示的是从0开始查询3条数据

六、关联
情况就是一对多，让两个表数据之间关联，一对多的关系，关联的字段在多的表里面，一个班级里面有多个学生，关联的字段就在学生的表里面，这个关联的字段就叫做外键
建表语句：
首先建立一张班级表：
create table class(id int auto_increment primary key,name varchar(20) not null,stuNum int not null);
在建立学生表：
create table student(id int auto_increment primary key,name varchar(20) not null,gender bit default 1,classid int nut null,foreihn
  key(classid) reference class(id));  foreign 表示的就是外键 reference表示的关联，后面加上关联的表名以及关联的健

插入一些数据：
insert into class values(0,"1",50),(0,"2",55)
insert into student values(0,"ana",1,10)   #此时会报错，因为班级ID里面没有数字是10 的

"""