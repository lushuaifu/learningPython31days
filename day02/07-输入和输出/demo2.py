'''
	input是一个函数，input('字符串')
	系统等待输入(阻塞)，回车enter之后，结束，并获取输入的值
'''
userName = input('请输入您的用户名：')
userPwd = input('请输入您的密码：')
#print('userName:%s'%userName)
#print('over......')
print('用户名-%s-， 密码-%s-'%(userName,userPwd))