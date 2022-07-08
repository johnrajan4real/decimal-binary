a=int(input('enter: '))
c={0}
d=0
while a>0:
    b=a%2
    a=a//2
    e=b*10**d
    d += 1
    c.add(e)
print(sum(c))