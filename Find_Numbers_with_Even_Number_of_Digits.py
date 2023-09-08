a=int(input())
b=input().split()
c=0
for i in b:
    if len(i)%2==0:
        c+=1
print(c)