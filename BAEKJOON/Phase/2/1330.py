# 두 수를 비교한 결과를 출력

A, B = map(int, input().split())

if A < B :
    print('<')
elif A > B :
    print('>')
else:
    print('==')