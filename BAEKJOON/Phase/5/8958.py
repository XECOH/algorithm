# OX퀴즈의 결과를 일차원 배열로 입력받아 점수를 계산하는 문제

for TC in range(int(input())):
    result = input()
    continued = 0
    score = 0
    for idx in range(len(result)):
        if result[idx] == 'O':
            score += 1
            if idx != 0:
                if result[idx-1] == 'O':
                    continued += 1
                    score += continued
                else:
                    continued = 0
    print(score)
