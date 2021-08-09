# 정수를 문자열로 입력받는 문제

N = int(input())
nums = input()

nums_sum = 0

for idx in range(N):
    nums_sum += int(nums[idx])

print(nums_sum)
