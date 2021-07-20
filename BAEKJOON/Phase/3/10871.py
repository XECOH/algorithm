# for와 if를 같이 쓰는 문제

N, X = map(int, input().split())
A = [map(int, input().split())]
ans = [num for num in A if num < A]
print(' '.join(map(str, ans)))