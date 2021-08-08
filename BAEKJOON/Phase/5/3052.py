# 2577.py 와 비슷한 문제

cnt_arr = [0 for _ in range(42)]

for _ in range(10):
    cnt_arr[int(input())%42] += 1

print(42-cnt_arr.count(0))
