# 문자열의 뒤에 A를 뺀다.
# B를 빼고 문자열을 뒤집는다.
S, T = input(), input()
answer = 0

while True:
    if len(T) == len(S):
        if T == S: answer = 1   
        break

    if T[-1] == "A":
        T = T[:-1]
    else:
        T = T[:-1][::-1]

print(answer)