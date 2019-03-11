names=['唐三藏','孙悟空']
#在末尾新增值
names.append('猪八戒')
print(names)
#插入到指定位置
names.insert(30,'沙悟净')
print(names)
names.insert(-2,'白龙马')
print(names)

monsters = ['大鹏鸟','犀牛精','xx']
#names.append(monsters)
#names.insert(1,monsters)
names.extend(monsters)
print(names)