import time
import  datetime

stime1 = '2015年10月20日'
#字符串--->时间time.struct_time
time1 = time.strptime(stime1,'%Y年%m月%d日')
print(time1)

#stime1 = time.strftime('%Y-%m-%d',time1)
#时间time.struct_time--->字符串
stime1 = time.strftime('%Y-%m-%d',time1)
print(stime1)



dt = datetime.datetime.now()
print(dt)

dt = datetime.date(2017,6,24)
#dt = datetime.datetime(2017,6,24,14,23,45)
print(str(dt))
print(type(dt))

print(dt.timetuple())

s = time.strftime('%Y/%m/%d',dt.timetuple())
print(s)
