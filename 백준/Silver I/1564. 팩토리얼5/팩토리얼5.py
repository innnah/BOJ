def factorial(n):
    num = 36288
    for i in range(10, n+1):
        num *= i
        while str(num)[-1] == "0":
            num //= 10
        num %= 100000000000000000
    
    return str(num)[-5:]

n = int(input())
print(factorial(n))