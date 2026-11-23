'The largest square has side length 3.'
n = int(input())
i = 0
while i*i <= n: i += 1
print(f"The largest square has side length {i-1}.")