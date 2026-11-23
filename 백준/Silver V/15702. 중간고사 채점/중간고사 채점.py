n, m = map(int, input().split())
questions = list(map(int, input().split()))
parti = [input().rstrip().split() for _ in range(m)]
parti = [[int(parti[i][0]), parti[i][1:]] for i in range(m)]
parti.sort()

maxScore = 0
num = parti[0][0]

for x in parti:
    score = 0
    for i in range(n):
        if x[1][i] == "O":
            score += questions[i]
    
    if score > maxScore:
        num = x[0]
        maxScore = score
        
print(num, maxScore)