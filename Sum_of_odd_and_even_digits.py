a=int(input())
b=list(map(int,input().split()))
c=0
d=0
for i in range(0,a):
    if i%2!=0:
        c+=b[i]
    else:
        d+=b[i]
if c==d:
    print("YES")
else:
    print("NO")
        