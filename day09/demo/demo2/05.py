'''
１．输入文件名，读取
２．将读取的信息写到一个文件中
３．关闭
'''
#读取文件内容
oldName = input('输入文件名：')
oldFile = open(oldName,'rb')
content = oldFile.read()
oldFile.close()

#得到新名
num = oldName.rindex('.')
newName = oldName[:num]+'-副本'+oldName[num:]

#写文件
newFile = open(newName,'wb')
newFile.write(content)
newFile.close()

print('哦了......')
