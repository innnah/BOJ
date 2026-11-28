n = int(input())
l = list(map(int, input().split()))
if l.count(0) >= (n+1)//2:
    print("INVALID")
else:
    if sum(l) > 0:
        print("APPROVED")
    else:
        print("REJECTED")