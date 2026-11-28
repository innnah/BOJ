import sys, bisect
input = sys.stdin.readline

cubes = []
for i in range(1, 1270):
    cubes.append(i**3)
for i in range(int(input())):
    a, b = map(int, input().split())
    print(f"Case #{i+1}: {bisect.bisect(cubes, b)-bisect.bisect_left(cubes, a)}")