# 달팽이의 움직임을 계산하는 문제

import math

A, B, V = map(int, input().split())
print(math.ceil((V-B)/(A-B)))
