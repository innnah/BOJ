import sys
input = sys.stdin.readline

n, m = map(int, input().split())
min = m*1440//n
print(f"{min//60:02d}:{min%60:02d}")