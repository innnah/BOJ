n = int(input())
l = [list(map(int, input().split())) for _ in range(n)]

def solution(idx, money = 0):
    if idx >= len(l):
        return money

    if idx+l[idx][0] <= len(l):
        return max(solution(idx+1, money), solution(idx+l[idx][0], money+l[idx][1]))
    else:
        return solution(idx+1, money)

print(solution(0))