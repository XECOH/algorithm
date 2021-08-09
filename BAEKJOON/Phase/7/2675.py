# 각 문자를 반복하여 출력하는 문제

for T in range(int(input())):
    R, S = input().split()
    P = ''
    for idx in range(len(S)):
        P += (S[idx]*int(R))
    print(P)