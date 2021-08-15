# 5와 3을 최소 횟수로 합하여 N을 만드는 문제

N = int(input())

result = 2000

for n in range((N//5)+1):
    r = N-(n*5)
    if r % 3 == 0:
        result = min(result, n+(r//3))

if result == 2000:
    print(-1)
else:
    print(result)