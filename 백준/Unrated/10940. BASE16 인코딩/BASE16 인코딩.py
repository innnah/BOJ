import base64

s = input().rstrip()
b = s.encode("utf-8")
e = base64.b16encode(b)
s1 = e.decode("UTF-8")
print(s1)