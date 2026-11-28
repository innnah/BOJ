import sys
input = sys.stdin.readline

n, m = map(int, input().split())
l = [list(map(int, input().split())) for _ in range(n)]
ret = 0
for i in range(n):
    arr = [0 for _ in range(n)]
    for j in range(1, n):
        if l[i][j-1] != l[i][j]:
            flag = False
            if abs(l[i][j-1]-l[i][j]) >= 2:
                break
            else:
                if l[i][j-1] > l[i][j]:
                    for k in range(j, j+m):
                        if k >= n or arr[k]:
                            flag = True
                            break
                        arr[k] = 1
                    if flag:
                        break
                else:
                    for k in range(j-m, j):
                        if k < 0 or arr[k]:
                            flag = True
                            break
                        arr[k] = 1
                    if flag:
                        break
    else:
        #print(1, i, arr)
        ret += 1
for i in range(n):
    arr = [0 for _ in range(n)]
    for j in range(1, n):
        if l[j-1][i] != l[j][i]:
            flag = False
            if abs(l[j-1][i]-l[j][i]) >= 2:
                break
            else:
                if l[j-1][i] > l[j][i]:
                    for k in range(j, j+m):
                        if k >= n or arr[k]:
                            flag = True
                            break
                        arr[k] = 1
                    if flag:
                        break
                else:
                    for k in range(j-m, j):
                        if k < 0 or arr[k]:
                            flag = True
                            break
                        arr[k] = 1
                    if flag:
                        break
    else:
        #print(2, i, arr)
        ret += 1
print(ret)