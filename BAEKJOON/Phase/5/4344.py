# 과연 그럴까요?

for C in range(int(input())):
    students = list(map(int, input().split()))
    scores = students[1:]
    avg = sum(scores) / students[0]
    over_avg = [score for score in scores if score > avg]
    print('%.3f'%round((len(over_avg)/students[0])*100, 3)+'%')
