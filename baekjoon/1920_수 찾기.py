from collections import defaultdict

N = int(input())
arr1 = list(map(int, input().split()))
dic = defaultdict(int)

for i in arr1:
    dic[i] = 1

M = int(input())
arr2 = list(map(int, input().split()))

for i in arr2:
    if dic[i] == 1:
        print(1)
    else:
        print(0)