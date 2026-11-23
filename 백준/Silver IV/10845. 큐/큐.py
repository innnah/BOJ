import sys

n = int(sys.stdin.readline().rstrip())
queue = []
for _ in range(n):
    order = sys.stdin.readline().rstrip().split()
    if order[0] == "push":
        queue.insert(0, int(order[1]))
    elif order[0] == "pop":
        print(queue.pop() if len(queue) != 0 else -1)
    elif order[0] == "front":
        print(queue[-1] if len(queue) != 0 else -1)
    elif order[0] == "back":
        print(queue[0] if len(queue) != 0 else -1)
    elif order[0] == "size":
        print(len(queue))
    elif order[0] == "empty":
        print(1 if len(queue) == 0 else 0)