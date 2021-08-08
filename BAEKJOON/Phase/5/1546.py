# 평균을 조작하는 문제

N = int(input())

scores = list(map(float, input().split()))

max_score = max(scores)

for idx in range(N):
    scores[idx] = (scores[idx] / max_score) * 100
  
print(sum(scores)/N)