def solution(priorities, location):
    answer = 0
    li = [i for i in range(len(priorities))]
    while True:
        if max(priorities) != priorities[0]:
            priorities.append(priorities.pop(0))
            li.append(li.pop(0))
        else:
            del li[0]
            del priorities[0]
            answer += 1
        
        try:
            li.index(location)
        except:
            break
    
    return answer

n = int(input())
for _ in range(n):
    a, b = map(int, input().split())
    p = list(map(int, input().split()))
    print(solution(p, b))