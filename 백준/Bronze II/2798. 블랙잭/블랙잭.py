best = -1
def choose(s, idx, remained=3):
    global best, n, m, cards
    if s > m: return
    if remained == 0: 
        best = max(best, s)
        return
    if idx == n: return
    for i in range(idx, n):
        choose(s + cards[i], i+1, remained-1)

n, m = map(int, input().split())
cards = list(map(int, input().split()))
choose(0, 0)
print(best)