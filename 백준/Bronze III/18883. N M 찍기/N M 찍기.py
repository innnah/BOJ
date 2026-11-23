import sys
print = sys.stdout.write
n,m=map(int,input().split())
for i in range(1,n+1):
    print(' '.join(map(str,list(range(m*(i-1)+1, m*i+1))))+"\n")