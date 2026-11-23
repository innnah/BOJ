def isCorrect(s):   
    stack = []
    opening = '(['
    for i in s:
        if i in opening:
            stack.append(i)
        elif i == ')':
            if len(stack) == 0 or stack[-1] != '(':
                return False
            stack.pop()
        elif i == ']':
            if len(stack) == 0 or stack[-1] != '[':
                return False
            stack.pop()
    if len(stack) != 0:
        return False
    return True

def getValue(s):
    if s == "()": return 2
    if s == "[]": return 3
    
    idx = -1
    stack = []
    ret = 0
    for i in range(len(s)):
        if idx == -1 and s[i] in ['(', '[']:
            idx = i
        if idx != -1:
            if s[idx] == '(':
                if s[i] == '(':
                    stack.append(s[i])
                elif s[i] == ')':
                    stack.pop()
            else:
                if s[i] == '[':
                    stack.append(s[i])
                elif s[i] == ']':
                    stack.pop()
        if len(stack) == 0:
            if s[idx+1:i] == "":
                value = 1
            else:
                value = getValue(s[idx+1:i])
            if s[idx] == "(":
                ret += 2 * value
            else:
                ret += 3 * value
            idx = -1
    
    return ret

s = input().rstrip()
if isCorrect(s):
    print(getValue(s))
else:
    print(0)