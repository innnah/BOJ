import sys

sys.setrecursionlimit(2147483647)

n = int(input())

def convert(n, base):
    T = "0123456789"
    q, r = divmod(n, base)
    if q == 0:
        return T[r]
    else:
        return convert(q, base) + T[r]
numlist = []
for i in range(2, 11):
    num = str(convert(n, i))
    if num == num[::-1]:
        numlist.append([i, num])
        
if len(numlist) == 0:
    print("NIE")
    exit()

for x in numlist:
    print(x[0], x[1])