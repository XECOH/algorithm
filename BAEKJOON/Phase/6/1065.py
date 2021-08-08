# X가 한수인지 판별하는 함수를 정의하여 문제를 해결해 봅시다.

def isHansu(num):
    if num < 10:
        y = num
    else :
        y = 9
        for n in range(10, num+1):
            diff = int(str(n)[1]) - int(str(n)[0])
            tmp = 0
            for idx in range(1, len(str(n))):
                tmp = int(str(n)[idx]) - int(str(n)[idx-1])
                if tmp != diff:
                    pass
            if tmp == diff:
                y += 1
    return y

N = int(input())

result = isHansu(N)
print(result)