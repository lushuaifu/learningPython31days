f = open('test.txt','r')
#按行读取全部，并将内容行组成列表集合
#lines = f.readlines()
#print(lines)
while True:
	line = f.readline()
	if line=='':
		break
	print('line:'+line)
