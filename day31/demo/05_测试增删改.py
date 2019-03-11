import mysqlHelper
import time

# 初始化对象
helper = mysqlHelper.MysqlHelper('127.0.0.1', 'root', '123456', 'python01')
# 连接
helper.connect()
# sql
sql = 'update t_user set name =%s,pwd=%s,birthday=%s where id=%s'
# params
id = input('输入编号:')
name = input('输入姓名:')
pwd = input('输入密码:')
birthday = time.strptime(input('输入生日:'), '%Y年%m月%d日')
params = [name, pwd, birthday,id]
# 执行
count = helper.update(sql, params)
# 判断
if count:
    print('成功。。。。。')
else:  # None,False,0
    print('失败。。。。。')
