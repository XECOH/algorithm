# 팩토리얼은 단순 for문으로도 구할 수 있지만, 학습을 위해 재귀를 써 봅시다.

def factorial(n, r):
    if n == 0:
        return r
    else:
        return factorial(n-1, r*n)

N = int(input())
print(factorial(N, 1))
