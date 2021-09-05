# 세 장의 카드를 고르는 모든 경우를 고려하는 문제

N, M = map(int, input().split())
cards = list(map(int, input().split()))

near = 0

for i in range(N):
    for j in range(i+1, N):
        for k in range(j+1, N):
            hap = cards[i]+cards[j]+cards[k]
            if hap <= M and hap > near:
                near = hap
                
print(near)