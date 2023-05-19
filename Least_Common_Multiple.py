m,n=map(int,input().split())
hcf=1
if m>n:
    c=n
else:
    c=m
for i in range(1,c+1):
    if n%i==0 and m%i==0:
        hcf=i
print((m*n)//hcf)