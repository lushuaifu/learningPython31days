import mysqlHelper

# 初始化对象
helper = mysqlHelper.MysqlHelper('127.0.0.1', 'root', '123456', 'python01')
# 连接
helper.connect()
# sql
sql = 'select * from t_user where name = %s and id > %s'
# params
params = ['老王',1]
# 执行
data = helper.fetchall(sql, params)
# 判断
if data:
    for temp in data:
        print(temp)
else:  # None,False,0
    print('没有数据。。。。。')
