import statistics as st
import sys

input = sys.stdin.readline

n = int(input())
l = [int(input()) for _ in range(n)]

print(int(round(st.mean(l), 0)))
print(st.median(l))
try: print(sorted(st.multimode(l))[1])
except IndexError: print(st.mode(l))
print(max(l)-min(l))