oldfileName=input('请输入要拷贝的文件名：')
oldfile=open(oldfileName,'rb')
#如果打开文件
if oldfile:
	#提取文件的后缀
	fileflagNum=oldfileName.rfind('.')
	if fileflagNum>0:
		fileflag=oldfileName[fileflagNum:]
	#组织新的文件名
	newfileName=oldfileName[:fileflagNum]+'[副本]'+fileflag
	#创建新文件
	newfile=open(newfileName,'wb')
	#把旧文件中的数据一行一行复制到新文件中
	for linecontent in oldfile.readlines():
		newfile.write(linecontent)
	oldfile.close()
	newfile.close()


