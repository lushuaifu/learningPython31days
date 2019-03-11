print('刷我滴卡---印度语，你好的意思')
print('呀咩跌---日语，不要的意思')

age = 10
name = '王宝强'
#+可以拼接两个字符串
print('名字是:'+name+',年龄是:'+str(age))
#  %s表示字符串的占位，%d表示整数的占位，%f表示浮点数的占位
ret = '名字是:%s，年龄是:%d'%(name,age)
ret = '名字是:%s'%name
ret = '名字是:%s，年龄是:%s'%(name,age)
print(ret)