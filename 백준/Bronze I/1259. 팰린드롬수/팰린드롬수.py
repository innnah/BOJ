while True:
    n = int(input())
    if n == 0:
        break
        
    if str(n)[::-1] == str(n):
        print("yes")
    else:
        print("no")