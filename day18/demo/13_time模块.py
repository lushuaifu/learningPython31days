import  time
import  random
#时间戳
print(time.time())
#本地：元组格式
print(time.localtime())
print(time.localtime())
t1 = time.localtime()
print(t1.tm_year)
print(t1.tm_mon)

#得到一定格式的时间
t = time.localtime()
print(type(t))
#时间转成字符串
s = time.strftime('%Y-%m-%d %H:%M:%S',t)
print(s)
print(type(s))
#字符串转时间
s = '2017-06-07 16:16:59'
t = time.strptime('2017年06月07日 16:16:59','%Y年%m月%d日 %H:%M:%S')
print(type(t))
print(t.tm_yday)


def f():
    time.sleep(random.randint(1,5))
    print('f.....')

t1 = time.mktime(time.localtime())
f()
t2 = time.mktime(time.localtime())

print(t1)
print(t2)
print(t2-t1)


t = time.localtime(1)
print(t)