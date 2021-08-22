# 분수의 순서에서 규칙을 찾는 문제

X = int(input())

# a = [int(n*(n+1)/2) for n in range(300)]
 
# def cart(N):
#     for i in range(len(a)):
#         if N <= a[i]:
#             break
#     return (N-a[i-1], i + 1 - (N-a[i-1]))
 
# def spot(x, y):
#     return a[x + y - 1] - (y-1)
 
# T = int(input())
# for t in range(1, T+1):
#     A, B = map(int,input().split())
#     (Ax, Ay) = cart(A)
#     (Bx, By) = cart(B)
#     C = spot(Ax+Bx, Ay+By)
#     print('#{} {}'.format(t, C))

n = 2

while True:
    if X < (((n**2)-n)//2)+1:
        d = (((n**2)-n)//2)+1 - X
        if n % 2:
            print(f'{n-d}/{d}')
        else:
            print(f'{d}/{n-d}')
        break
    else:
        n += 1