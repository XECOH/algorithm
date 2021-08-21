# 2부터 X-1까지 모두 나눠서 X가 소수인지 판별하는 문제 2

M = int(input())
N = int(input())

sum_pn = 0
min_pn = 10000

for n in range(M, N+1):
    cnt = 1
    for h in range(2, n+1):
        if n % h == 0:
            cnt += 1
        if cnt > 2:
            break
    if cnt == 2:
        sum_pn += n 
        min_pn = min(min_pn, n)

if sum_pn == 0:
    print(-1)
else:
    print(f'{sum_pn}\n{min_pn}')