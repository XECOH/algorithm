# 벌집이 형성되는 규칙에 따라 벌집의 위치를 구하는 문제

N = int(input())
n = 2

if N == 1:
    print(1)
else:
    while True:
        if N < 3*((n-1)**2)-(3*(n-1))+2:
            print(n-1)
            break
        elif N == 3*((n-1)**2)-(3*(n-1))+2:
            print(n)
            break
        else:
            n += 1         