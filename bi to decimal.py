a=input('enter: ')
b=len(a)
d={0}
for i in a:
    b-=1
    if int(i)==1:
        c=(2**b)
        d.add(c)
print(sum(d))