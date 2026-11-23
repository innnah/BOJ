strings = []
while True:
    try:
        strings.append(input().rstrip().split())
    except:
        break
        
for x in strings:
    for i in x[0]:
        index = x[1].find(i)
        if index == -1:
            print("No")
            break
        if index != len(x[1]) - 1:
            x[1] = x[1][index + 1:]
    else:
        print("Yes")