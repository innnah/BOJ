import sys
input = sys.stdin.readline

def distance(p1, p2):
    return (p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2

def divconq(left, right):
    if right - left == 1:
        return distance(points[left], points[right])
    if right - left == 2:
        return min(distance(points[left], points[left + 1]),
                   distance(points[left + 1], points[right]),
                   distance(points[left], points[right]))
    
    mid = (left + right) // 2
    min_dist = min(divconq(left, mid), divconq(mid + 1, right))

    mid_line = points[mid][0] + 0.5
    cand = []
    for i in range(left, right + 1):
        if (points[i][0] - mid_line) ** 2 < min_dist:
            cand.append(points[i])
    cand.sort(key=lambda x: x[1])
    for i in range(len(cand)):
        for j in range(i + 1, len(cand)):
            if (cand[j][1] - cand[i][1]) ** 2 >= min_dist:
                break
            min_dist = min(min_dist, distance(cand[i], cand[j]))
    return min_dist

n = int(input())
points = [list(map(int, input().split())) for _ in range(n)]
points.sort()
print(divconq(0, n - 1))