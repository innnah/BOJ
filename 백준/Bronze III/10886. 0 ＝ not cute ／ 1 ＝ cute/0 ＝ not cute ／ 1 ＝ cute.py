n = int(input())
not_cute = 0
cute = 0
for _ in range(n):
    if int(input()): cute += 1
    else: not_cute += 1

if not_cute > cute: print("Junhee is not cute!")
else: print("Junhee is cute!")