# 함수 d를 정의하여 문제를 해결해 봅시다.

def selfnumber():
    nums = [0 for _ in range(10001)]
    for num in range(1, 10001): 
        tmp = num
        for idx in range(len(str(num))):
            tmp += int(str(num)[idx])
        if tmp < 10001:
            nums[tmp] += 1
    for idx in range(1, 10001):
        if nums[idx] == 0:
            print(idx)

selfnumber()
