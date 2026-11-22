import sys
input = sys.stdin.readline

for _ in range(int(input())):
    n, m = map(int, input().split())
    black = [list(map(int, input().split())) for _ in range(n)]
    white = [list(map(int, input().split())) for _ in range(m)]

    black_lines = [[-black[i][0], black[i][1]] for i in range(n)]
    white_lines = [[-white[i][0], white[i][1]] for i in range(m)]
    points = [-50000]
    for i in range(n):
        for j in range(m):
            a1, b1 = black_lines[i]
            a2, b2 = white_lines[j]
            if a1 == a2:
                continue
            x = (b2 - b1) / (a1 - a2)
            points.append(x)
    points.append(50000)
    points = sorted(set(points))
    ans = 0
    for i in range(len(points)-1):
        x = (points[i] + points[i+1]) / 2
        black_y = [black_lines[j][0] * x + black_lines[j][1] for j in range(n)]
        white_y = [white_lines[j][0] * x + white_lines[j][1] for j in range(m)]
        if max(black_y) < min(white_y) or min(black_y) > max(white_y): ans = 1
    print("YES" if ans else "NO")