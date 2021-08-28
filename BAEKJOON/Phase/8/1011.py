# 거리에 따른 장치 사용 횟수를 출력하는 문제

for T in range(int(input())):
    x, y = map(int, input().split())
    d = y - x
    n = int((y-x)**0.5)
    if d == n**2 :
        print(2*n-1)
    elif n**2 < d <= n**2 + n :
        print(2*n)
    elif d > n**2 + n :
        print(2*n+1)