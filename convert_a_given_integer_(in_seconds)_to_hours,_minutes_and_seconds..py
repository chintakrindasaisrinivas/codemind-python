a=int(input())
b=a//3600
c=(a%3600)//60
d=((a%3600)%60)
print("H:M:S-%d:%d:%d"%(b,c,d))