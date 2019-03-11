'''
    python操作mysql进行增删改查的封装

    1、增删改，代码类似
    2、查询

    代码分析
    1、获取连接对象
    2、sql语句不同，参数不同
    3、获取执行对象
        增删改
        查询
            1、fetchone
            2、fetchall
    4、处理结果
    5、关闭

    面向对象  建立类，封装属性和函数
'''
import pymysql


class MysqlHelper:
    '''python操作mysql的增删改查的封装'''
    def __init__(self, host, user, password, database, port=3306, charset='utf8'):
        '''
        初始化参数
        :param host:        主机
        :param user:        用户名
        :param password:    密码
        :param database:    数据库
        :param port:        端口号，默认是3306
        :param charset:     编码，默认是utf8
        '''
        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password
        self.charset = charset

    def connect(self):
        '''
        获取连接对象和执行对象
        :return:
        '''
        self.conn = pymysql.connect(host=self.host,
                                    user=self.user,
                                    password=self.password,
                                    database=self.database,
                                    port=self.port,
                                    charset=self.charset)

        self.cur = self.conn.cursor()

    def fetchone(self, sql, params=()):
        '''
         根据sql和参数获取一行数据
       :param sql:          sql语句
       :param params:       sql语句对象的参数元组，默认值为()
       :return:             查询的一行数据
       '''
        dataOne = None
        try:
            count = self.cur.execute(sql, params)
            if count != 0:
                dataOne = self.cur.fetchone()
        except Exception as ex:
            print(ex)
        finally:
            self.close()
        return dataOne

    def fetchall(self, sql, params=()):
        '''
         根据sql和参数获取一行数据
       :param sql:          sql语句
       :param params:       sql语句对象的参数元组，默认值为()
       :return:             查询的一行数据
       '''
        dataall = None
        try:
            count = self.cur.execute(sql, params)
            if count != 0:
                dataall = self.cur.fetchall()
        except Exception as ex:
            print(ex)
        finally:
            self.close()
        return dataall

    def close(self):
        '''
        关闭执行工具和连接对象
        '''
        if self.cur != None:
            self.cur.close()
        if self.conn != None:
            self.conn.close()
