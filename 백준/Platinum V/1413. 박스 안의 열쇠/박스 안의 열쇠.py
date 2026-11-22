from fractions import Fraction as F
p=print
n,k=map(int,input().split())
n+=1
d=[[0]*n for _ in range(n)]
d[0][0]=1
for i in range(n-1):
    for j in range(1,n):d[i+1][j]=d[i][j]*i+d[i][j-1]
r=str(F(sum(d[-1][:k+1]),sum(d[-1])))
if r=='1':p("1/1")
else:p(r)