# 피보나치 수 역시 단순 for문으로도 구할 수 있지만, 학습을 위해 재귀를 써 봅시다.

def fibonacci(f):
    if f == 0:
        return 0
    elif f == 1 or f == 2:
        return 1
    else:
        return fibonacci(f-2) + fibonacci(f-1)

n = int(input())
print(fibonacci(n))