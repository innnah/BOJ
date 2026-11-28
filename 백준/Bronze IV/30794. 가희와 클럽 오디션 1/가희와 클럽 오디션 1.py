import sys
input = sys.stdin.readline

n, s = input().rstrip().split()
n = int(n)
if s == 'miss': print(0)
elif s == 'bad': print(n*200)
elif s == 'cool': print(n*400)
elif s == 'great': print(n*600)
else: print(n*1000)