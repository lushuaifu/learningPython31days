num=int(input('请输入一个分数'))
if 0<=num<60:
    print('D')
elif num<80:
    print('C')
elif num<90:
    print('B')
elif num<=100:
    print('A')
else:
    print('您的输入错误')
