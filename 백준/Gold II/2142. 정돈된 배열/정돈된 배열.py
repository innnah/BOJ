import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    diff = []
    for i in range(1, m):
        diff.append(arr[0][i] - arr[0][i-1])
    for i in range(1, n):
        flag = False
        for j in range(1, m):
            if diff[j-1] < arr[i][j] - arr[i][j-1]:
                flag = True
                break
        if flag:
            print("NO")
            break
    else:
        print("YES")