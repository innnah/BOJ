l = list(map(int, input().split()))
scores = [100, 100, 200, 200, 300, 300, 400, 400, 500]
for i in range(9):
    if l[i] > scores[i]:
        print("hacker")
        exit(0)
if sum(l) >= 100: print("draw")
else: print("none")