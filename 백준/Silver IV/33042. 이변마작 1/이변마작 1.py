from collections import defaultdict

n = int(input())
arr = input().split()
d = defaultdict(int)
for i in range(n):
    d[arr[i]] += 1
    if d[arr[i]] == 5:
        print(i+1)
        break
else:
    print(0)