# N번째 종말의 수가 나올 때까지 차례대로 시도하는 문제

N = int(input())

n = 1
num = 666
while True:
    if '666' in str(num) and n == N:
        print(num)
        break
    elif '666' in str(num) and n != N:
        n += 1
        num += 1
    else:
        num += 1
