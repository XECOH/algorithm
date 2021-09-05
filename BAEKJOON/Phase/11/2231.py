# 모든 경우를 시도하여 N의 생성자를 구하는 문제

N = int(input())

M = 1

while M < N :
    m = str(M)
    hap = M
    for n in range(len(m)):
        hap += int(m[n])
    if hap == N:
        break
    else:
        M += 1

if M == N :
    print(0)
else:
    print(M)