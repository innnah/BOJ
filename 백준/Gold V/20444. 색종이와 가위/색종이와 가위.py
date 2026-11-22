a, b = map(int, input().split())
a += 2
lo = 1
hi = a//2
while lo <= hi:
    mid = (lo+hi)//2
    val = mid * (a-mid)
    if val == b:
        print("YES")
        exit(0)
    elif val < b:
        lo = mid+1
    else:
        hi = mid-1
print("NO")