# 주어진 단어에서 가장 많이 사용된 알파벳을 출력하는 문제

word = input().lower()

cnt = [word.count(chr(idx+97)) for idx in range(26)]

if cnt.count(max(cnt)) > 1:
    print('?')
else:
    print(chr(cnt.index(max(cnt))+97).upper())


