# 입력이 끝날 떄까지 A+B를 출력하는 문제. EOF에 대해 알아 보세요.

# EOF (End of File) - 데이터 소스로부터 더 이상 읽을 수 있는 데이터가 없음을 나타내는 용어

import sys

lines = sys.stdin.readlines()
l = len(lines)
c = 0
while True:
    if l == c:
        break
    else:
        print(sum(map(int, lines[c].split())))
        c += 1