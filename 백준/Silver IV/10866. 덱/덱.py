import sys
input = sys.stdin.readline

def push_front(x):
    deq.insert(0, x)
def push_back(x):
    deq.append(x)
def pop_front():
    if not deq: print(-1)
    else: print(deq.pop(0))
def pop_back():
    if not deq: print(-1)
    else: print(deq.pop())
def size():
    print(len(deq))
def empty():
    print(0 if deq else 1)
def front():
    if not deq: print(-1)
    else: print(deq[0])
def back():
    if not deq: print(-1)
    else: print(deq[-1])

n = int(input())
deq = []
for _ in range(n):
    s = input().rstrip().split()
    order = s[0]
    if order == "push_front": push_front(s[1])
    elif order == "push_back": push_back(s[1])
    elif order == "pop_front": pop_front()
    elif order == "pop_back": pop_back()
    elif order == "size": size()
    elif order == "empty": empty()
    elif order == "front": front()
    elif order == "back": back()