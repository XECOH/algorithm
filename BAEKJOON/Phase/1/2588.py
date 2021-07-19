# 빈 칸에 들어갈 수는 ?

three_digits1, three_digits2 = input(), input()
answer = 0
for idx in range(-1, -4, -1):
    tmp = int(three_digits1)*int(three_digits2[idx])
    answer += tmp*(10**(abs(idx)-1))
    print(tmp)
print(answer)