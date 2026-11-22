import sys
input = sys.stdin.readline

dr = {"L" : 0, "R" : 0, "D" : 1, "U" : -1}
dc = {"L" : -1, "R" : 1, "D" : 0, "U" : 0}
def isInside(r, c): return 0 <= r < n and 0 <= c < m

n, m = map(int, input().split())
board = [list(input().rstrip()) for _ in range(n)]
op = input().rstrip()

mon_cnt = 1
item_cnt = 0
for i in range(n):
    for j in range(m):
        if board[i][j] == '&':
            mon_cnt += 1
        elif board[i][j] == 'B':
            item_cnt += 1
monsters = {}
for _ in range(mon_cnt):
    tmp = input().rstrip().split()
    for i in range(7):
        if i != 2:
            tmp[i] = int(tmp[i])
    tmp[0] -= 1; tmp[1] -= 1
    monsters[(tmp[0], tmp[1])] = tmp[2:]

item_chests = {}
for _ in range(item_cnt):
    tmp = input().rstrip().split()
    for i in range(2): tmp[i] = int(tmp[i])
    if tmp[2] != "O":
        tmp[3] = int(tmp[3])
    tmp[0] -= 1; tmp[1] -= 1
    item_chests[(tmp[0], tmp[1])] = tmp[2:]

r, c = -1, -1
sr, sc = -1, -1
for i in range(n):
    for j in range(m):
        if board[i][j] == "@":
            r, c = i, j
            sr, sc = i, j
board[sr][sc] = '.'

love = 1
exp = 0
at, df = 0, 0
hp = 20
acc = set()

idx = 0
end_message = "Press any key to continue."
while idx < len(op):
    query = op[idx]
    nr, nc = r + dr[query], c + dc[query]
    if isInside(nr, nc) and board[nr][nc] != "#":
        if board[nr][nc] == "^":
            hp -= 5
            if "DX" in acc: hp += 4
            if hp <= 0:
                if "RE" not in acc:
                    end_message = "YOU HAVE BEEN KILLED BY SPIKE TRAP.."
                    idx += 1
                    break
                else:
                    hp = 5*love + 15
                    r, c = sr, sc
                    acc.remove("RE")
                    idx += 1
                    continue
            r, c = nr, nc
        elif board[nr][nc] in ("&", "M"):
            if board[nr][nc] == "M" and "HU" in acc:
                hp = love*5+15
            r, c = nr, nc
            stat = monsters[(r, c)]
            p_at = max(1, love*2+at-stat[2])
            m_at = max(1, stat[1]-(love*2+df))
            m_hp = stat[3]
            turn = 0
            while hp > 0 and m_hp > 0:
                if board[nr][nc] == "M" and "HU" in acc and turn == 1: hp += m_at
                if turn % 2 == 0:
                    if turn == 0:
                        if "CO" in acc:
                            tmp_at = (love*2+at)*2
                            if "DX" in acc: tmp_at += tmp_at//2
                            tmp_at = max(1, tmp_at-stat[2])
                            m_hp -= tmp_at
                            m_hp += p_at
                    m_hp -= p_at
                else: hp -= m_at
                turn += 1
            if hp <= 0:
                if "RE" not in acc:
                    end_message = f"YOU HAVE BEEN KILLED BY {stat[0]}.."
                    idx += 1
                    break
                else:
                    hp = 5*love + 15
                    r, c = sr, sc
                    acc.remove("RE")
                    idx += 1
                    continue
            else:
                if "HR" in acc:
                    hp = min(love*5+15, hp+3)
                if "EX" in acc:
                    exp += int(stat[4] * 1.2)
                else:
                    exp += stat[4]
                if exp >= 5*love:
                    exp = 0
                    love += 1
                    hp = love*5+15
                if board[r][c] == "M":
                    end_message = "YOU WIN!"
                    idx += 1
                    break
                board[r][c] = '.'
        elif board[nr][nc] == "B":
            r, c = nr, nc
            stat = item_chests[(r, c)]
            if stat[0] == "O":
                if len(acc) < 4:
                    acc.add(stat[1])
            elif stat[0] == "W":
                at = stat[1]
            else:
                df = stat[1]
            board[r][c] = '.'
        else:
            r, c = nr, nc
    else:
        if board[r][c] == '^':
            hp -= 5
            if "DX" in acc: hp += 4
            if hp <= 0:
                if "RE" not in acc:
                    end_message = "YOU HAVE BEEN KILLED BY SPIKE TRAP.."
                    idx += 1
                    break
                else:
                    hp = 5*love + 15
                    r, c = sr, sc
                    acc.remove("RE")
                    idx += 1
                    continue
    idx += 1

if end_message[4] != 'H':
    board[r][c] = '@'
for i in board:
    print(''.join(i))
print(f"Passed Turns : {idx}")
print(f"LV : {love}")
print(f"HP : {max(0, hp)}/{love*5+15}")
print(f"ATT : {love*2}+{at}")
print(f"DEF : {love*2}+{df}")
print(f"EXP : {exp}/{love*5}")
print(end_message)