while True:
    s = input()
    cnt = 0
    
    if s == "#":
        break
        
    for x in s:
        if x.lower() in ['a', 'e', 'i', 'o', 'u']:
            cnt += 1
            
    print(cnt)