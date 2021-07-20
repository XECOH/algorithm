# 1부터 N까지의 합을 구하는 문제. 물론 반복문 없이 풀 수도 있습니다.

ans = 0
for n in range(1, int(input())+1):
    ans += n
print(ans)