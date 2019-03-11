a=list(range(5))
print(a)
b=[x for x in range(5)]
print(b)
c=[x*2 for x in range(5)]
print(c)
d=[x for x in range(10) if x%2==0]
print(d)

e=(x for x in range(5) )
print(e)
print(next(e))

f=(x for x in range(5) )
for i in f:
    print(i)

g=[[x,y] for x in range(5) for y in range(5)]
print(g)

h=[(x,y) for x in range(5) for y in range(5)]
print(h)

k=([x,y] for x in range(5) for y in range(5))
for i in k:
    print(i)

l=((x,y) for x in range(5) for y in range(5))
for i in l:
    print(i)