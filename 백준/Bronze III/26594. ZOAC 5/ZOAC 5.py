import sys
input = sys.stdin.readline
def gcd(a,b):
    while b != 0:
        a,b=b,a%b
    return a
s=input().rstrip()
l=[]
tmp=1
for i in range(1,len(s)):
    if s[i] != s[i-1]:
        l.append(tmp)
        tmp=1
    else:
        tmp+=1
ret=tmp
for i in l:
    ret=gcd(ret,i)
print(ret)