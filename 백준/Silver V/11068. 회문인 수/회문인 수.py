def convert(n, base):
    nums = []
    num = n 
    while num != 0:
        nums.append(num % base)
        num //= base
        
    return nums[::-1]

for _ in range(int(input())):
    n = int(input())
    for i in range(2, 65):
        nums = convert(n, i)
        if nums[::-1] == nums:
            print(1)
            break
    else:
        print(0)