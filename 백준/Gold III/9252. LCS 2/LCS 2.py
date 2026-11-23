import sys
input = sys.stdin.readline

def matchStringIter():
    cache = [[0 for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]
    for i in range(1, len(s1)+1):
        for j in range(1, len(s2)+1):
            if s1[i-1] == s2[j-1]:
                cache[i][j] = cache[i-1][j-1] + 1
                choices[i][j] = (i-1, j-1)
            else:
                if cache[i-1][j] > cache[i][j-1]:
                    cache[i][j] = cache[i-1][j]
                    choices[i][j] = (i-1, j)
                else:
                    cache[i][j] = cache[i][j-1]
                    choices[i][j] = (i, j-1)
    return cache[-1][-1]

def reconstruct(a, b):
    if choices[a][b][0] == -1 and choices[a][b][1] == -1: return ""
    add = ""
    if s1[a-1] == s2[b-1]: add = s1[a-1]
    return reconstruct(choices[a][b][0], choices[a][b][1]) + add
            
s1, s2 = input().rstrip(), input().rstrip()
choices = [[(-1,-1)] * (len(s2)+1) for _ in range(len(s1)+1)]
print(matchStringIter())
print(reconstruct(len(s1), len(s2)))