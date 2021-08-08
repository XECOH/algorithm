# 최댓값이 어디에 있는지 찾는 문제

max_value, max_index = 0, 0
for idx in range(9):
    num = int(input())
    if max_value < num:
        max_value, max_index = num, idx+1
print(f'{max_value}\n{max_index}')