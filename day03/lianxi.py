#计算交税
salary=int(input('请输入您的工资'))
num=salary-3500
rate=0
if num>0:
    print('收税')
    if num<=1500:
        rate=0.03
    elif num<=4500:
        rate=0.1
    elif num<=9000:
        rate=0.2
    elif num<=35000:
        rate=0.25
    elif num<=55000:
        rate=0.3
    elif num<=80000:
        rate=0.35
    else:
        rate=0.45
    tax=num*rate
    salary1=salary-tax
    print('实际所得工资是%d  ''税率是%0.2f  ''税是%0.2f'%(salary1,rate,tax))
else:
    print('不收税')
