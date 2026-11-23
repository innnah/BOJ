import sys

sys.setrecursionlimit(1000000)

n = int(input())

def solve(n):
    if n % 5 == 0:
        return n // 5

    if n - 5 >= 3:
        tmp = solve(n - 5)
        if tmp != -1:
            return tmp + 1
        
        if n % 3 != 0:
            return -1
        
        return n // 3
    
    if n % 3 == 0:
        return n // 3

    return -1

print(solve(n))