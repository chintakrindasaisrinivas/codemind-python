a=int(input())
b=list(map(int,input().split()))
c=[]
d=0
for i in range(0,a):
    for j in range(0,a):
        if b[i]>=b[j] and i!=j and b[i]!=b[j]:
            d+=1
    c.append(d)
    d=0
print(*c)