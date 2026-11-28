import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
if sum(arr) % 2:
    print(1)
else:
    s = 0
    for i in range(n-1):
        s += arr[i]
        if s % 2 == 0:
            print(1)
            break
    else:
        print(0)