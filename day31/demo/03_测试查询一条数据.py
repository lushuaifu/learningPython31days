import mysqlHelper

# 初始化对象
helper = mysqlHelper.MysqlHelper('127.0.0.1', 'root', '123456', 'python01')
# 连接
helper.connect()
# sql
sql = 'select * from t_user where id = %s'
#sql = 'select * from t_user where id = 1'
# params
params = [2]
# 执行
data = helper.fetchone(sql, params)
#data = helper.fetchone(sql)
# 判断
if data:
    print(data)
else:  # None,False,0
    print('没有数据。。。。。')
