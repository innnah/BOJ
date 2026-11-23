from collections import deque
import sys, itertools

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    order = input().rstrip()
    n = int(input())
    s = input().rstrip()[1:-1]
    rev = 0
    broke = 0
    if s != "":
        deq = deque(list(map(int, s.split(","))))
    else:
        deq = deque([])

    for c in order:
        if c == "D":
            if len(deq) == 0:
                print("error")
                broke = 1
                break
            else:
                if rev % 2: 
                    deq.pop()
                else:
                    deq.popleft()
        if c == "R":
            rev += 1
    
    if not broke:    
        if rev % 2:
            deq.reverse()
        print('[', end = '')
        if len(deq) != 0:
            for i in list(itertools.islice(deq, 0, len(deq)-1)):
                print(i, end = ',')
            print(deq[-1], end = '')
        print(']')