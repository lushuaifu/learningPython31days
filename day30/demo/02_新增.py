# 导入python操作mysql的模块
import pymysql

# 获取连接对象
conn = pymysql.connect(host='127.0.0.1', user='root', password='123456', database='python01', port=3306, charset='utf8')
# 获取执行工具
cur = conn.cursor()
# sql语句,增删改
sql = 'insert into t_user(name,pwd,birthday) values("老王","123456",str_to_date("2017年10月20日","%Y年%m月%d日"))'
# 执行,返回值。如果是增删改，返回受影响的行数，如果是查询，返回查询的行数
count = cur.execute(sql)
#提交
conn.commit()
print('受影响的行数:%s'%count)
# 关闭
cur.close()
conn.close()
