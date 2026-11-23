H, M = map(int, input().split())

if H == 0 and M < 45:
    H += 24

minute = H * 60 + M
new_minute = minute - 45

print(new_minute // 60, new_minute % 60)