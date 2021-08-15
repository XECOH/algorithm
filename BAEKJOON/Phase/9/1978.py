# 2부터 X-1까지 모두 나눠서 X가 소수인지 판별하는 문제 1

N = int(input())
nums = list(map(int, input().split()))

cnt = 0

for n in range(N):
    num = nums[n]
    a = 1
    for h in range(2, num+1):
        if num % h == 0:
            a += 1
            if a > 2:
                break
    if a == 2:
        cnt += 1

print(cnt)

