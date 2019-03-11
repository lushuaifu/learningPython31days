'''
try:
    #num = 100
    print(num)
except NameError as errorMsg:
    print('产生错误了:%s'%errorMsg)
else:
    print('没有捕获到异常，真高兴')
print('over...')
'''

try:
    num = 100
    print num
except Exception as ex:
    print('产生错误了:%s'%ex)
else:
    print('没有捕获到异常，真高兴')
print('over...')

