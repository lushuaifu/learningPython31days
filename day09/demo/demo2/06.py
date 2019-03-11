'''
１．输入文件名，读取
２．将读取的信息写到一个文件中
３．关闭

如果是大文件，直接读取完，对内存有影响，所以一次读一部分，写一部分
循环：
１．循环体
	读一点，写一点
２．循环条件
	判断读取的内容是不是'',如果是就退出循环
'''
#读取文件内容
oldName = input('输入文件名：')
oldFile = open(oldName,'rb')

#得到新名
num = oldName.rindex('.')
newName = oldName[:num]+'-副本'+oldName[num:]

#写文件
newFile = open(newName,'wb')

#循环
while True:
	content = oldFile.read(1024)
	if content=='':
		break
	newFile.write(content)

#关闭
oldFile.close()
newFile.close()

print('哦了......')
