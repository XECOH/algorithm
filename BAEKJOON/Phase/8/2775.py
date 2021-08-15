# 층과 거주자 수의 규칙을 찾는 문제 

for T in range(int(input())):
    k = int(input())
    n = int(input())
    numerator, denominator = 1, 1
    for f in range(k+1):
        numerator *= (f+n)
        denominator *= (f+1)
    print(numerator // denominator)