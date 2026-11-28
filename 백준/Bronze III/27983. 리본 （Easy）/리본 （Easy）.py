import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = input().rstrip().split()
for i in range(n):
    flag = False
    for j in range(n):
        if c[i] != c[j]:
            if abs(a[i]-a[j]) <= b[i]+b[j]:
                print("YES")
                print(i+1, j+1)
                flag = True
                break
    if flag: break
else:
    print("NO")