# 빠르게 입력받고 출력하는 문제

# 시간 초과 
for T in range(int(input())):
    A, B = map(int, input().split())
    print(A+B)

# sys.stdin.readline 사용
import sys

for T in range(int(input())):
    A, B = map(int, sys.stdin.readline.split())
    print(A+B)