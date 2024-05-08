import math, random
n=4
m=3
a=[]
for i in range(n):
    a.append([])
    for j in range(m):
        a[i].append(random.randint(0,1))
print(a)
for x in a:
    for h in x:
        y=math.sin(h)
        print(y)