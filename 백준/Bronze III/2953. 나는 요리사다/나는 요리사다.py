scores = [list(map(int, input().split())) for _ in range(5)]
sums = []

for i in range(5):
    sums.append([sum(scores[i]), i+1])

sums.sort()
print(sums[4][1], sums[4][0])