# 크로아티아 알파벳의 개수를 세는 문제

croatia_alphabet = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

word = input()

cnt = 0

for idx in range(len(croatia_alphabet)):
    cnt += word.count(croatia_alphabet[idx])

print(len(word)-cnt)

