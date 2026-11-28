def get_pos(depth):
    if depth == 0: return [0, 0]
    p = get_pos(depth-1)
    if arr[n-depth] >= 3:
        p[0] += 2 ** (depth-1)
    if arr[n-depth] % 3 == 1:
        p[1] += 2 ** (depth-1)
    return p
def get_str(depth):
    if depth == 0: return ''
    s = ""
    s1, s2 = np[0] >= 2 ** (depth-1), np[1] >= 2 ** (depth-1)
    if not s1 and not s2:
        s += '2'
    elif s1 and not s2:
        s += '3'
    elif not s1 and s2:
        s += '1'
    else:
        s += '4'
    np[0] -= s1 * (2 ** (depth-1))
    np[1] -= s2 * (2 ** (depth-1))
    s += get_str(depth-1)
    return s

n, s = map(int, input().split())
arr = list(map(int, str(s)))
c, r = map(int, input().split())
r = -r
p = get_pos(n)
np = [p[0] + r, p[1] + c]
if 0 <= np[0] < 2 ** n and 0 <= np[1] < 2 ** n:
    print(get_str(n))
else:
    print(-1)