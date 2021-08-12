# 호텔 방 번호의 규칙을 찾아 출력하는 문제

for T in range(int(input())):
    H, W, N = map(int, input().split())
    f, n = 0, 0
    if N % H == 0:
        f, n = H, N//H
    else:
        f, n = N % H, (N // H)+1
    print(str(f)+str('%02d'%n))