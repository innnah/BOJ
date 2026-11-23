import sys
input = sys.stdin.readline

factorials = [1,2,6,24,120]
while True:
    n = input().rstrip()
    if n == "0":
        break
    
    num = 0
    for i in range(len(n)):
        num += factorials[i] * int(n[::-1][i])
        
    print(num)