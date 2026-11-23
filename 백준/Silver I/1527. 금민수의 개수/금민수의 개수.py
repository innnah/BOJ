a, b = map(int, input().split())

def solution(depth=0, num=0):
    global a, b
    answer = 0
    if depth >= 10:
        return 0
    if num > b:
        return 0
    if a <= num <= b:
        answer += 1
    
    answer += solution(depth+1, num*10+4)
    answer += solution(depth+1, num*10+7)

    return answer

print(solution())