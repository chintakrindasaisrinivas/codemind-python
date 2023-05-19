a,b=map(int,input().split())
s=0
for i in range(a,b+1):
    c=i**(1/2)
    s=s+c
print("%0.2f"%s)