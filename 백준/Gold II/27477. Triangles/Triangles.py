import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n = int(input())
    arr = [list(map(int, input().rstrip())) for _ in range(n)]
    ans = [0 for _ in range(10)]
    r_end = [[10000, -1] for _ in range(10)]
    c_end = [[10000, -1] for _ in range(10)]
    for i in range(n):
        for j in range(n):
            c_end[arr[i][j]][0] = min(c_end[arr[i][j]][0], j)
            c_end[arr[i][j]][1] = max(c_end[arr[i][j]][1], j)
            r_end[arr[i][j]][0] = min(r_end[arr[i][j]][0], i)
            r_end[arr[i][j]][1] = max(r_end[arr[i][j]][1], i)
    for i in range(10):
        for j in range(n):
            s, e = -1, -1
            for k in range(n):
                if arr[j][k] == i:
                    s = k
                    break
            for k in range(n-1, -1, -1):
                if arr[j][k] == i:
                    e = k
                    break
            if s == -1:
                continue
            side = max(n-1-s, e)
            height1 = max(j - r_end[i][0], r_end[i][1] - j)
            height2 = max(n-1-j, j)
            ans[i] = max(ans[i], max(height2*(e-s), side*height1))
            #print(j, side, height1, height2, s, e)

        for j in range(n):
            s, e = -1, -1
            for k in range(n):
                if arr[k][j] == i:
                    s = k
                    break
            for k in range(n-1, -1, -1):
                if arr[k][j] == i:
                    e = k
                    break
            if s == -1:
                continue
            side = max(n-1-s, e)
            height1 = max(j - c_end[i][0], c_end[i][1] - j)
            height2 = max(n-1-j, j)
            ans[i] = max(ans[i], max(height2*(e-s), side*height1))
            #print(j, side, height1, height2, s, e)
        #print()
    print(*ans)