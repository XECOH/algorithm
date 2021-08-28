# 모든 사람을 비교하여 덩치 등수를 구하는 문제

N = int(input())

result = [0 for _ in range(N)]
people = []

for _ in range(N):
    people.append(list(map(int, input().split())))

for p1 in range(N):
    for p2 in range(N):
        if p1 == p2:
            pass
        else:
            if people[p1][0] > people[p2][0] and people[p1][1] > people[p2][1]:
                result[p2] += 1

for res in result:
    print(res+1, end=' ')

