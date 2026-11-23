n = int(input())
if n == 1:
    print("*")
    exit()
i = 1
down = False
while True:
    print("*" * i)
    if not down:
        i += 1
        if i == n:
            down = True
    else:
        i -= 1
        
    if i == 1:
        break
        
        
print("*")