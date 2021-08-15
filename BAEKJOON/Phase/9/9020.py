# 소수 응용 문제 2

prime_number = [0, 0] + [1 for _ in range(10001)]

for n in range(2, 101):
    for h in range(2*n, 10001, n):
        prime_number[h] = 0

for T in range(int(input())):
    n = int(input())
    gb_1, gb_2 = 0, 0
    diff = 10000
    for h in range(2, n+1):
        if prime_number[h] == 0:
            pass
        else:
            if prime_number[n-h] == 1:
                if diff >= abs(n-(2*h)):
                    gb_1, gb_2 = h, n-h
                    diff = n-(2*h)
                else:
                    pass
    print(f'{min(gb_1, gb_2)} {max(gb_1, gb_2)}')

