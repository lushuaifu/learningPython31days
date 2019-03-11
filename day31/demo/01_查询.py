# 导入python操作mysql的模块
import pymysql

# 获取连接对象
conn = pymysql.connect(host='127.0.0.1', user='root', password='123456', database='python01', port=3306, charset='utf8')
# 获取执行工具
cur = conn.cursor()
# sql语句,增删改
#sql = 'select birthday from t_user'
sql = 'select id,name,pwd,birthday from t_user'
# 执行,返回值。如果是增删改，返回受影响的行数，如果是查询，返回查询的行数
count = cur.execute(sql)
print('查询的结果有%s条数据'%count)

#获取第一行
# dateOne = cur.fetchone()
# print(dateOne)

#向上移动一行
#cur.scroll(-1)

#向下移动一行
#cur.scroll(1)

#cur.scroll(1,mode='absolute')
#cur.scroll(1,mode='relative')

#获取所有行的数据
dataAll = cur.fetchall()
#print(dataAll)

# for temp in dataAll:
#     print(temp)
# print(dataAll[-1][2])


# for temp in cur:
#     print(temp)


s = 'id:%s,name:%s,pwd:%s,birthday:%s'
for temp in dataAll:
    print(s%(temp[0],temp[1],temp[2],temp[3]))

# 关闭
cur.close()
conn.close()
