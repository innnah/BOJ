scores = [int(input()) for _ in range(5)]

for x in scores:
    if x < 40:
        scores[scores.index(x)] = 40

print(f'{sum(scores) // 5}')