n=int(input())
a=list(map(int,input().split()))
s=set(a)
c=[]
for i in s:
    if a.count(i)==1:
        c.append(i)
if len(c)==0:
    print(-1)
else:
    print(*c)