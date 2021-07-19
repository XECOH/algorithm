# 네 개의 계산식을 계산하는 문제

A, B, C = map(int, input().split())

print((A+B)%C)
print(((A+B)%C)%C)
print((A*B)%C)
print(((A*B)%C)%C)