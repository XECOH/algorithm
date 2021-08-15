# 직사각형과 점의 거리를 구하는 문제

x, y, w, h = map(int, input().split())

print(min(y-h, x, x-w, y))
