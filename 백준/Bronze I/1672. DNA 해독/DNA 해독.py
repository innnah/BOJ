import sys
input = sys.stdin.readline

arr = {"A":0, "G":1, "C":2, "T":3}
matching = [['A', 'C', 'A', 'G'], ['C', 'G', 'T', 'A'], ['A', 'T', 'C', 'G'], ['G', 'A', 'G', 'T']]
n = int(input())
s = list(input().rstrip())
for i in range(1, n):
    s[n-i-1] = matching[arr[s.pop()]][arr[s[n-i-1]]]
print(s[0])