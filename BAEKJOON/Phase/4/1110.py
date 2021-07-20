# 원래 수로 돌아올 때까지 연산을 반복하는 문제

c = 0
N = int(input())
tmp = N
while True:
    if len(str(tmp)) < 2:
        if N == (2*tmp):
            c += 1
            print(c)
            break
        else:
            tmp *= 2
            c += 1
    else:
        if str(N) == str(tmp)[1]+str(int(str(tmp)[0])+int(str(tmp)[1]))[1]:
            c += 1
            print(c)
            break
        else:
            tmp = int(str(tmp)[1]+str(int(str(tmp)[0])+int(str(tmp)[1]))[1])
            c += 1