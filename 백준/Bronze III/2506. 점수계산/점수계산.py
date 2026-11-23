n = int(input())
OXlist = list(map(int, input().split()))

score = 0
upscore = 1

for x in OXlist:
    if x == 1:
        score += upscore
        upscore += 1
    else:
        upscore = 1
        
print(score)