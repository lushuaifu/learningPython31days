# 导入python操作mysql的模块
import pymysql
import time

# 获取连接对象
conn = pymysql.connect(host='127.0.0.1', user='root', password='123456', database='python01', port=3306, charset='utf8')
# 获取执行工具
cur = conn.cursor()
# sql语句,增删改，sql注入
sql = 'insert into t_user(name,pwd,birthday) values(%s,%s,%s)'
# 参数列表
name = input('输入姓名:')
pwd = input('输入密码:')
birthday = input('输入生日:')      # 2017年10月01日--->日期struct_time(--->2017-10-01)
birthday = time.strptime(birthday,'%Y年%m月%d日')
#print(type(birthday))   <class 'time.struct_time'>


params = [name,pwd,birthday]
# 执行,返回值。如果是增删改，返回受影响的行数，如果是查询，返回查询的行数
count = cur.execute(sql,params)
#提交
conn.commit()
print('受影响的行数:%s'%count)
# 关闭
cur.close()
conn.close()


'''
    select name,pwd from t_user where name = 'xx' and pwd = 'xx'
    select name,pwd from t_user where name = 'abc' or '1==1' and pwd = 'abc' or '1==1'

    abc' or '1==1
'''