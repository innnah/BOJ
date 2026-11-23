import math

n = int(input())
if int(math.log2(n)) == math.log2(n):
    print(n)
    exit()

l = [i for i in range(1, n+1)]

while len(l) != 1:
    l = l[1::2].copy()

print(l[0])