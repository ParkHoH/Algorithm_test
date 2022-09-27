# 그리디 문제
# 앞 자리수가 최대가 되도록 구현
# dict에서 해당 숫자에 대한 자리수의 합을 구하고 가장 큰 순서대로 순위를 부여함
from collections import defaultdict

N = int(input())
dic = defaultdict(int)

for _ in range(N):
    string = input()[::-1]

    for i, s in enumerate(string):
        dic[s] += 10**i

L = sorted(dic.values(), reverse=True)
result = 0
idx = 9

for num in L:
    result += num * idx
    idx -= 1

print(result)