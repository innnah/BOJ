n = int(input())
arr = set(input().split())
arr2 = set(input().split())
for i in arr:
    if i not in arr2:
        print(i)