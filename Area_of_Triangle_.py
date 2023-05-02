import math
a,b,c=map(int,input().split())
s=(a+b+c)/2
cs=(s*(s-a)*(s-b)*(s-c))
print("%0.2f"%(cs**(1/2)))