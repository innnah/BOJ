import sys

input = sys.stdin.readline

def gcd(a, b):
    while b != 0:
        a, b = b, a%b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

n = int(input())
tmp = [list(map(int, input().split())) for _ in range(n)]
l = [[i[0] // gcd(i[0], i[1]), i[1] // gcd(i[0], i[1])] for i in tmp]
up = []

downlcm = l[0][1]
for i in l:
    downlcm = lcm(downlcm, i[1])

for i in l:
    i[0] *= downlcm // i[1]

ret = l[0][0]
for i in l:
    ret = gcd(i[0], ret)

print(ret, downlcm)