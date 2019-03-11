name = '旺财小强旺旺旺小明丁丁'
#查找字符第一次出现的位置,找不到返回-1
index1 = name.find('小s')
print(index1)
#print(name[1],name[-1])

index1 = name.find('小',0,len(name))
print(index1)

index1 = name.find('小',2,4)
print(index1)


#从右开始查
index1 = name.rfind('小')
print(index1)

index1 = name.rfind('小',2,8)
print(index1)

#查找字符第一次出现的位置,找不到报错
index1 = name.index('小')
print(index1)

#查找出现的次数
count = name.count('旺旺')
print(count)


file = 'D:\\work\\python\\2017-05-08\\day06\\video\\01_课程回顾.avi'
print(file)
#分割,将分割的后的内容组合成list
ret = file.split('\\')
print(ret,type(ret))
print(ret[-1])

file = 'D:\\work\\python\\2017-05-08\\day06\\video\\01_课程回顾.avi'
print(file)
#分割,将分割的后的内容组合成list
ret = file.split('\\',2)
print(ret,type(ret))

files = '床前明月光\r\n疑是地上霜\n举头望明月\n低头思故乡'
print(files)
ret = files.splitlines()
#ret = files.split('\n')
print(ret,type(ret))


name = '旺财小强旺旺旺小明丁丁'
#分割，得到三部分
ret = name.partition('旺旺')
ret = name.rpartition('旺旺')
print(ret,type(ret))