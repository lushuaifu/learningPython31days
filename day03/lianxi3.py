import random
player=int(input('剪刀（0），石头（1），布（2），请输入一个数字'))  

while 1:
    computer=random.randint(0,2)
    if player<0 or player>2:
        print('您的输入错误，请输入0-2之间的数')
        player=int(input('请输入重新一个数字'))
        continue
    if (player==0 and computer==2)or(player==1 and computer==0)or(player==2 and computer==1):
        print('您赢啦！还想继续吗？yes or no')
    elif player==computer:
        print('平局，还想继续吗？yes or no')
    else:
        print('您输啦！，还想继续吗？yes or no')
    player=input('请输入yes or no')
    if player=='yes':
        player=int(input('请输入一个数字'))
    else:
        break
    
 
