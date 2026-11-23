s = input()
d = {1: "YES", 0: "NO"}
idx = s.find("=")
es = s[:idx]
print(d[eval(es) == int(s[idx+1:])])