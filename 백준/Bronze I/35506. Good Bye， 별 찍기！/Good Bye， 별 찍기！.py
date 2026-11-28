n = int(input())
for i in range(n*2):
    print(" "*(n*2-1-i)+"*"+" "*(i+1)+" "*int(abs(n-0.5-i))+"*"+" "*int(n*2-abs(n-0.5-i)*2)+"*"+" "*int(abs(n-0.5-i)))
