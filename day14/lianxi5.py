try:
    num=100
    print(num)
except NameError as errorMsg:
    print('产生错误了：%s'%errorMsg)
else:
    print('没有捕捉到异常，真高兴')