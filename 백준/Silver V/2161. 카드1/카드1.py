stack = [i for i in range(1, int(input())+1)]

while len(stack) > 0:
    print(stack.pop(0), end = ' ')
    try:
        stack.append(stack.pop(0))
    except:
        pass