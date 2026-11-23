a, b = map(int, input().split())
n = int(input())
numlist = list(map(int, input().split()))
base10 = 0
nums = []

for i in range(n):
    base10 += numlist[i] * (a ** (n - i - 1))

while base10 > 0:
    nums.insert(0, base10 % b)
    base10 //= b

for x in nums:
    print(x, end = ' ')