# 규칙에 따라 문자에 대응하는 수를 출력하는 문제

nums = {'ABC': 3, 'DEF': 4, 'GHI': 5, 'JKL': 6, 'MNO': 7, 'PQRS': 8, 'TUV': 9, 'WXYZ': 10}

word = input()

min_time = 0

for idx in range(len(word)):
    for key in nums:
        if word[idx] in key:
            min_time += nums[key]
            pass

print(min_time)