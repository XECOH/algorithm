# A+B를 바로 위 문제보다 아름답게 출력하는 문제

for T in range(1, int(input())+1):
    A, B = map(int, input().split())
    print(f'Case #{T}: {A} + {B} = {A+B}')