s1='abcd1234'
t1=s1.startswith('a')
print(t1)
t1=s1.startswith('a',1,5)
print(t1)
t2=s1.endswith('4')
print(t2)
t2=s1.endswith('4',2,6)
print(t2)
print()

s2='abcd12345'
print(s2.isalnum())
s3='anhgf'
print(s3.isalpha())
s4='456123'
print(s4.isdigit())
s5='GHSF'
print(s5.isupper())
s6='gdhsjakju'
print(s6.islower())
s7='    '
print(s7.isspace())
s8='abc'
print(s8.capitalize())
print(s8.upper())
s9='bgAB'
print(s9.lower())
#返回一个原字符串左对齐,并使用空格填充至长度 width 的新字符串
s10='床前明月光'
print(s10.ljust(10),end='')
print('_'*5)
print(s10.rjust(30))
print(s10.center(20))

s11='abc   123   '
print(s11.strip())
s12='3bc123'
print(s12.strip('3'))
print(s12.lstrip('3'))
print(s12.rstrip('3'))


s13={'1','2','3'}
print('_'.join(s13))

s14='a中'
print(s14.encode('utf-8'),type(s14.encode('utf-8')))   #结果s14=b'a\xe4\xb8\xad'

s15=b'a\xe4\xb8\xad'
print(s15.decode('utf-8'))

