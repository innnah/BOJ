import sys
input = sys.stdin.readline

def count_jump(fs, fe):
    jcnt = 0
    vids, vide = fs // l, fe // l
    jcnt += psum[l-1] * (vide - vids)
    jcnt -= psum[fs % l - 1]
    jcnt += psum[fe % l]
    return jcnt

n, l, k = map(int, input().split())
jumps = list(map(int, input().split()))
jumps = [x-1 for x in jumps]
psum = [0 for _ in range(l)]
for j in jumps:
    psum[j] += 1
for i in range(1, l):
    psum[i] += psum[i-1]
psum.append(0)

frames = [0, 0]
speed = 1
fcnt = 1
while frames[-1] < l*n-1:
    fcnt += 1
    speed += count_jump(frames[0], frames[1])
    frames[0] = frames[1]+1
    frames[1] = frames[0] + speed - 1
print(fcnt)