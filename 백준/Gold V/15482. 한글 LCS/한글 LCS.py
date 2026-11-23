import sys

input = sys.stdin.readline

def matchStringIter():
    cache = [[0 for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]
    for i in range(1, len(s1)+1):
        for j in range(1, len(s2)+1):
            if s1[i-1] == s2[j-1]:
                cache[i][j] = cache[i-1][j-1] + 1
            else:
                cache[i][j] = max(cache[i-1][j], cache[i][j-1])
    return cache[-1][-1]
            
s1, s2 = input().rstrip(), input().rstrip()
print(matchStringIter())