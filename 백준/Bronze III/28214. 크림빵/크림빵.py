i=lambda:map(int,input().split())
n,k,m = i()
l=list(i())
ret=0
for j in range(n):ret+=l[j*k:k*(j+1)].count(0)<m
print(ret)