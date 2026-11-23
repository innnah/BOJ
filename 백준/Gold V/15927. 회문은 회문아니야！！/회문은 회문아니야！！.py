s = input().rstrip()

if len(list(set(s))) == 1:
    print(-1)
    exit(0)
elif s[::-1] != s:
    print(len(s))
    exit(0)

start = 0; end = len(s) - 2
minus = 2
answer = -1
while start != end:
    if s[start:end+1:-1] != s[start:end+1]:
        answer = end - start + 1
        break
    else:
        if end + 1 == len(s):
            minus += 1
            start = 0
            end = len(s) - minus
        else:
            start += 1
            end += 1
            
print(answer)