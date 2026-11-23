n = int(input())
cnt = 0

def ishan(n):
    a = str(n)
    
    if len(a) <= 2:
        return True
    
    sub = int(a[0]) - int(a[1])
    
    for i in range(1, len(a)-1):
        if int(a[i]) - int(a[i+1]) != sub:
            return False
    else:
        return True
    
for i in range(1, n + 1):
    if ishan(i):
        cnt += 1
        
print(cnt)