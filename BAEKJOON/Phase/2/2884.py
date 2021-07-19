# 시간 뺄셈 문제

H, M = map(int, input().split())

if M >= 45:
    print(f'{H} {M-45}')
else :
    if H == 0:
        H = 24
    print(f'{H-1} {M+15}')