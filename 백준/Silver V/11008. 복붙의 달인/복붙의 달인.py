for _ in range(int(input())):
    s, sub = input().split()
    length = len(sub)
    cnt = 0
    cnt += s.count(sub)
    cnt += len(s) - length * cnt
    
    print(cnt)