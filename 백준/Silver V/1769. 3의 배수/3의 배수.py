n = list(map(int, list(input())))

def isMul3(n, count = 0):
    if len(n) == 1:
        return count, not n[0] % 3
    
    total = sum(n)
    return isMul3(list(map(int, list(str(total)))), count + 1)

ismul3 = isMul3(n)
print(ismul3[0])
if ismul3[1]:
    print("YES")
else:
    print("NO")