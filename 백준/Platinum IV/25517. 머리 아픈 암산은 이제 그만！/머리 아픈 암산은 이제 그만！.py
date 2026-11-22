import sys
input = sys.stdin.readline
M=10**9+7
u=200000000
l=[1,933245637,429277690,724464507,203191898,698611116]
n,m=map(int,input().split())
j=n//u
f=l[j]
for i in range(j*u+1,n+1):f*=i;f%=M
a=set(int(input()) for _ in range(m))
k=1
for i in a:k*=i;k%=M
b=pow(k,M-2,M)
print((f*b)%M)