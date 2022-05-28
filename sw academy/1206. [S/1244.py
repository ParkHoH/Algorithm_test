from collections import defaultdict

TC = int(input())
for case in range(TC):
    dic = defaultdict(list)
    num, n = map(int, input().split())
    stack = list(map(int, str(sorted(num, reverse=True))))
    num = list(map(int, str(num)))
    for i in range(len(str(num))):
        dic[num[i]].append(i)

    print(f'#{case+1} ')