# 조건에 맞는 문자열을 찾는 문제

cnt = 0

for N in range(int(input())):
    word = list(input())
    if word == sorted(word, key=word.find):
        cnt += 1
        
print(cnt)
