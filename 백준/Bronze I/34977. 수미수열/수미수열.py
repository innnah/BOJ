n = int(input())
arr = list(map(int, input().split()))
for k in range(1, n//2+1):
    if arr[:k] == arr[-k:]:
        print("yes")
        break
else:
    print("no")