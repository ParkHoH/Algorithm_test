from collections import defaultdict

TC = int(input())
for case in range(TC):
    dic = defaultdict(list)
    num, n = map(int, input().split())
    stack = list(map(int, str(sorted(num, reverse=True))))
    num = list(map(int, str(num)))
    

    print(f'#{case+1} ')