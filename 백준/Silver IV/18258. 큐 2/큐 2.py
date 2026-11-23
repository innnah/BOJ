from sys import stdin

input()
s, orders = [], stdin.readlines()
cnt = 0

for x in orders:
    command = x.split()
    if command[0] == "push":
        s.append(command[1])
    elif command[0] == "pop":
        if len(s) > cnt:
            print(s[cnt])
            cnt += 1
        else: print(-1)
    elif command[0] == "size":
        print(len(s) - cnt)
    elif command[0] == "empty":
        print(0 if len(s) > cnt else 1)
    elif command[0] == "front":
        if len(s) > cnt: print(s[cnt])
        else: print(-1)
    elif command[0] == "back":
        if len(s) > cnt: print(s[-1])
        else: print(-1)