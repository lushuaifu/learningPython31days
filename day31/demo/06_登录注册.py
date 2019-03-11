from mysqlHelper import MysqlHelper
import hashlib


def login():
    '''登录'''
    name = input('输入用户名:')
    pwd = input('输入密码:')
    #加密
    pwd = doPwd(pwd)

    helper = MysqlHelper('127.0.0.1', 'root', '123456', 'python01')
    helper.connect()
    sql = 'select * from t_user where name=%s and pwd=%s'
    params = [name, pwd]
    data = helper.fetchone(sql, params)
    if data:
        print('登录成功。。。。。')
    else:  # None,False,0
        print('登录失败。。。。。')


def doPwd(pwd):
    '''sha1编码'''
    mysha1 = hashlib.sha1()
    mysha1.update(pwd.encode('utf-8'))
    pwd = mysha1.hexdigest()
    return pwd


def register():
    '''注册'''
    name = input('输入用户名:')
    pwd = input('输入密码:')
    # 加密
    pwd = doPwd(pwd)


    helper = MysqlHelper('127.0.0.1', 'root', '123456', 'python01')
    helper.connect()
    sql = 'insert into t_user(name,pwd) values(%s,%s)'
    params = [name, pwd]
    count = helper.insert(sql, params)
    if count:
        print('成功。。。。。')
    else:  # None,False,0
        print('失败。。。。。')


if __name__ == '__main__':
    #register()
    login()
