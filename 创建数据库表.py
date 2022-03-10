import pymysql
db=pymysql.connect(host="localhost",user="root",password="182515131", db="Ana")
cursor=db.cursor()
#检查表是否存在，如果存在则删除
cursor.execute("drop table if exists")



cursor.close()
db.close()