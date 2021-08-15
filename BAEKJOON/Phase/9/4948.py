# 소수 응용 문제 1

prime_number = [0, 0] + [1 for _ in range(246913)]

for n in range(2, 246913):
    for h in range(2*n, 246913, n):
        prime_number[h] = 0

while True:
    n = int(input())
    if n == 0:
        break
    else:
        print(prime_number[n+1: 2*n+1].count(1))
        pass        


