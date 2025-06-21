import sys
sys.stdin = open("nquanhau.inp")
sys.stdout = open("nquanhau.out", "w")

queen_icon = "\u2655"
n = int(input())
board = [['.' for _ in range(n+1)] for _ in range(n+1)]
def show(table: list[list]):
    global n
    for i in range(1, n+1):
        for j in range(1, n+1):
            print(table[i][j], end=" ")
        print()
    print("---------------")
def check(i, j) -> bool:
    # column check
    for k in range(1, n+1):
        if board[k][j] == queen_icon:
            return False
    # diagonal check
    x = i
    y = j
    while x < n and y < n:
        x += 1
        y += 1
        if board[x][y] == queen_icon:
            return False
    x = i
    y = j
    while x < n and y > 1:
        x += 1
        y -= 1
        if board[x][y] == queen_icon:
            return False
    x = i
    y = j
    while x > 1 and y < n:
        x -= 1
        y += 1
        if board[x][y] == queen_icon:
            return False
    x = i
    y = j
    while x > 1 and y > 1:
        x -= 1
        y -= 1
        if board[x][y] == queen_icon:
            return False
    return True
cnt = 0
def Try(i):
    global cnt
    for j in range(1, n+1):
        if board[i][j] == '.':
            if check(i, j):
                board[i][j] = queen_icon
                if i == n:
                    show(board)
                    cnt += 1
                else:
                    Try(i + 1)
                board[i][j] = '.'


Try(1)
print(cnt)


