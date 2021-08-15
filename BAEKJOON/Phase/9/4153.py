# 피타고라스의 정리에 대해 배우는 문제

while True:
    [a, b, c] = sorted(list(map(int, input().split())))
    if [a, b, c].count(0) == 3:
        break
    if a**2 + b**2 == c**2:
        print('right')
    else:
        print('wrong')
        

