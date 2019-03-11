dict={'001':'天空','002':'黑夜','003':'杭州'}
for key in dict:
    print('%s:%s'%(key,dict[key]))
print()
for key in dict.keys():
    print('%s:%s'%(key,dict[key]))
print()

for k,v in dict.items():
    print('%s:%s'%(k,v))
