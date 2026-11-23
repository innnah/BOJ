for _ in range(3):
    s = input().rstrip()
    l = []
    cnt = 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            cnt += 1
        else:
            l.append(cnt)
            cnt = 1
    l.append(cnt)
    print(max(l))