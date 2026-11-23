n = int(input())
OXlist = [input() for _ in range(n)]

def OXscore(OXstring):
    upscore = 1
    score = 0

    for i in OXstring:
        if i == "O":
            score += upscore
            upscore += 1
        else:
            upscore = 1

    return score

for s in OXlist:
    print(OXscore(s))