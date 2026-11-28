import sys
input = sys.stdin.readline

isPrime = [1 for _ in range(100003)]
isPrime[0] = 0
isPrime[1] = 0
for i in range(2, 501):
    if isPrime[i]:
        for j in range(i**2, 100003, i):
            isPrime[j] = 0

special = [1 for _ in range(100001)]
special[0] = 0
for n in range(1, 100001):
    sn = str(n)
    for i in range(1, len(sn)):
        if isPrime[int(sn[:i]) * int(sn[i:]) + 1] == 0:
            special[n] = 0
            break
    if isPrime[n+1] == 0:
        special[n] = 0

for i in range(1, 100001):
    special[i] += special[i-1]
for _ in range(int(input())):
    n = int(input())
    print(special[n])