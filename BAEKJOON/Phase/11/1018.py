# 체스판을 만드는 모든 경우를 시도하여 최적의 방법을 찾는 문제

N, M = map(int, input().split())
board = [list(input()) for _ in range(N)]

cnt = []

for h in range(N-7):
    for w in range(M-7):
        B = 0
        W = 0
        for dh in range(h, h+8):
            for dw in range(w, w+8):
                if (dh+dw) % 2:
                    if board[dh][dw] != 'B':
                        W += 1
                    if board[dh][dw] != 'W':
                        B += 1
                else:
                    if board[dh][dw] != 'B':
                        B += 1
                    if board[dh][dw] != 'W':
                        W += 1
        cnt.append(B)
        cnt.append(W)

print(min(cnt))