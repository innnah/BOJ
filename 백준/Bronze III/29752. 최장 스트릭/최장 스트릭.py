import sys
input = sys.stdin.readline

days = int(input())
solved = list(map(int, input().split()))
streak = 0
max_streak = 0
for i in range(days):
    if solved[i] == 0:
        max_streak = max(max_streak, streak)
        streak = 0
    else:
        streak += 1
print(max(max_streak, streak))