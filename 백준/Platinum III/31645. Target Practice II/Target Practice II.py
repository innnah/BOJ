import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, x = map(int, input().split())
    rects = [list(map(int, input().split())) for _ in range(n)]
    arr = list(map(int, input().split()))
    arrm, arrp = [], []
    for i in range(4*n):
        if arr[i] < 0:
            arrm.append(arr[i])
        else:
            arrp.append(arr[i])
    if len(arrm) < n or len(arrp) < n:
        print(-1)
        continue
    arrm.sort()
    arrp.sort()
    point_m = [[rects[i][2] * (-arrm[0]) + rects[i][1], rects[i][1], rects[i][2]] for i in range(n)]
    point_p = [[rects[i][2] * (-arrp[n-1]) + rects[i][0], rects[i][0], rects[i][2]] for i in range(n)]
    point_f = [[rects[i][0], x] for i in range(n)] + [[rects[i][1], x] for i in range(n)]
    point_f.sort()
    for i in range(len(arrm)-n):
        a, b = point_f[i]
        point_m.append([b*(-arrm[0])+a, a, b])
    for i in range(len(arrm)-n, 2*n):
        a, b = point_f[i]
        point_p.append([b*(-arrp[n-1])+a, a, b])

    top, bottom = -10**100, 10**100
    point_m.sort()
    point_p.sort()
    #print(point_m, point_p)
    for i in range(len(arrm)):
        top = max(top, point_m[i][2] * (-arrm[i]) + point_m[i][1])
    for i in range(len(arrp)):
        bottom = min(bottom, point_p[i][2] * (-arrp[i]) + point_p[i][1])
    
    print(top-bottom)