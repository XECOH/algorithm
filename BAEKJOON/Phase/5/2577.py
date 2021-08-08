# 각 숫자가 몇 번 나왔는지 저장하기 위해 일차원 배열을 만드는 문제

nums = 1

for _ in range(3):
    nums *= int(input())

nums = str(nums)
for idx in range(10):
    print(f'{nums.count(str(idx))}')