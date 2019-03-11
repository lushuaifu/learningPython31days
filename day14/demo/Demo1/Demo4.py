try:
    print('try......')
    num = 10
    a = 1/0
except Exception as ex:
    print('except......')
    print('num:%s'%num)
    print('ex:%s'%ex)

print('over......')
print('num:%s'%num)
#print(ex)


