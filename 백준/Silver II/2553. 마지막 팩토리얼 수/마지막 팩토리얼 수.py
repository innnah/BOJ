import math
n = int(input())
a = str(math.factorial(n))
for i in range(len(a)-1, -1, -1):
    if a[i] != "0":
        print(a[i])
        break