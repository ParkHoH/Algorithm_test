N = int(input())
dic = {}
for i in map(int, input().split()):
    dic[i] = 1

M = int(input())
for i in map(int, input().split()):
    if i in dic:
        print(1, end=" ")
    else:
        print(0, end=" ")
