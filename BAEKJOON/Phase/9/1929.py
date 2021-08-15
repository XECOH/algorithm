# 에라토스테네스의 체로 풀어 봅시다.

M, N = map(int, input().split())

prime_number = [0, 0] + [1 for _ in range(N+1)]

for n in range(2, N+1):
    for h in range(2*n, N+1, n):
        prime_number[h] = 0

for idx in range(M, N+1):
    if prime_number[idx] == 1:
        print(idx)
