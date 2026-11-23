import sys

input = sys.stdin.readline

a1 = [1, 3, 6, 10, 15, 21]
a2 = [5000000, 3000000, 2000000, 500000, 300000, 100000]
b1 = [1, 3, 7, 15, 31]
b2 = [5120000, 2560000, 1280000, 640000, 320000]

n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    money = 0
    if a != 0:
        for i in range(6):
            if a <= a1[i]:
                money += a2[i]
                break
    if b != 0:
        for i in range(5):
            if b <= b1[i]:
                money += b2[i]
                break
    print(money)