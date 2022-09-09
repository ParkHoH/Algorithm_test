S = input()
dic = {"0": 0, "1": 0}
dic[S[0]] += 1

for i in range(1, len(S)):
    if S[i] != S[i-1]:
        dic[S[i]] += 1

print(min(dic["0"], dic["1"]))