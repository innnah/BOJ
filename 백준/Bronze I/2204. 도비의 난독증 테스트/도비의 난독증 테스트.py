while True:
    n = int(input())
    if n == 0:
        break
        
    original = [input() for _ in range(n)]
    words = [original[i].rstrip().lower() for i in range(n)]
    words.sort()
    
    for x in original:
        if x.rstrip().lower() == words[0]:
            print(x)