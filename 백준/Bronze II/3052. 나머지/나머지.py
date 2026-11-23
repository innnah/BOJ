'''
1
2
3
4
5
6
7
8
9
10
'''

numlist = [int(input()) % 42 for _ in range(10)]

tmp = set(numlist)

result = list(tmp)

print(len(result))