l = [[], [], ["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"], ["J", "K", "L"], ["M", "N", "O"], ["P", "Q", "R", "S"], ["T", "U", "V"],
["W", "X", "Y", "Z"]]

s = input()
cnt = 0

for x in s:
    for i in range(10):
        if x in l[i]:
            cnt += i + 1
            break

print(cnt)