# 한 단어에서 각 알파벳이 처음 등장하는 위치를 찾는 문제

S = input()

alphabet = [0 for _ in range(26)]

for idx in range(26):
    if chr(idx+97) not in S:
        alphabet[idx] = -1
    else:
        alphabet[idx] = S.index(chr(idx+97))

print(' '.join(map(str, alphabet)))

