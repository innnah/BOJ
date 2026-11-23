import sys
input = sys.stdin.readline
s = input().rstrip()
l = input().rstrip().split()
news = ""
for i in s:
    if i in l:
        news += chr(ord(i)+32)
    else:
        news += i
print(news)