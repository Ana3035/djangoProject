import pymysql
#链接数据库

db=pymysql.connect(host="localhost",user="root",
                     password="182515131", db="Ana")

#创建一个cursor对象
cursor=db.cursor()
sql="select version()"
#执行sql语句
cursor.execute(sql)
#获取返回的信息
data=cursor.fetchone()
print(data)
#断开
cursor.close()
db.close()