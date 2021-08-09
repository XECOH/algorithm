# 숫자를 뒤집어서 비교하는 문제

A, B = map(str, input().split())
A, B = A[::-1], B[::-1]

print(max(int(A), int(B)))