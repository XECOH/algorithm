# N을 소인수 분해하는 문제

N = int(input())

for n in range(2, N+1):
    if N % n != 0:
        pass
    else:
        while True:
            print(n)
            N = N // n 
            if N % n != 0:
                break
      