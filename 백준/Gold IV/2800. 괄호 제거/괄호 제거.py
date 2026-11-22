import sys
input = sys.stdin.readline

s = input().rstrip()
stack = []
bracket = []
for i in range(len(s)):
    if s[i] == '(':
        stack.append((s[i], i))
    elif s[i] == ')':
        bracket.append((stack[-1][1], i))
        stack.pop()
status = [-1 for _ in range(len(s))]
for i in range(len(bracket)):
    status[bracket[i][0]] = i
    status[bracket[i][1]] = i
ret = set()
for i in range(2**len(bracket)):
    string = ""
    for j in range(len(s)):
        if status[j] != -1:
            if i & (1 << status[j]):
                string += s[j]
        else:
            string += s[j]
    ret.add(string)
ret = list(ret)
ret.sort()
for i in ret:
    if i != s:
        print(i)