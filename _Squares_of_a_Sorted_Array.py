a=int(input())
b=list(map(int,input().split()))
c=sorted(b)
e=0
d=[]
for i in range(0,a):
    e=b[i]**2
    d.append(e)
    e=0
print(*sorted(d))
    