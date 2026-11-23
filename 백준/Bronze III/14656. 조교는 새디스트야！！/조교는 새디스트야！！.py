n = int(input())
l = list(map(int,input().split()))
cnt=0
for i in range(n):
    if l[i]!=i+1:cnt+=1
print(cnt)