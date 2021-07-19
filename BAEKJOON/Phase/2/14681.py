# 점이 어느 사분면에 있는지 알아내는 문제

x, y = int(input()), int(input())

if x > 0 and y > 0 :
    print(1)
elif x > 0 and y < 0 :
    print(4)
elif x < 0 and y > 0 :
    print(2)
else :
    print(3)