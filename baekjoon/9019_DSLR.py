from collections import deque
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    start, target = map(int, input().split())

    dic = {}
    queue = deque()
    queue.append([start, ""])

    while queue:
        num, comb = queue.popleft()

        # D
        new_num = (num * 2) % 10000
        if new_num == target:
            print(comb + "D")
            break

        if new_num not in dic:
            dic[new_num] = 1
            queue.append([new_num, comb+"D"])

        # S
        new_num = num-1 if num != 0 else 9999
        if new_num == target:
            print(comb + "S")
            break

        if new_num not in dic:
            dic[new_num] = 1
            queue.append([new_num, comb+"S"])

        # L
        str_num = str(num).zfill(4)
        new_num = int(str_num[1] + str_num[2] + str_num[3] + str_num[0])
        if new_num == target:
            print(comb + "L")
            break

        if new_num not in dic:
            dic[new_num] = 1
            queue.append([new_num, comb+"L"])

        # R
        new_num = int(str_num[3] + str_num[0] + str_num[1] + str_num[2])
        if new_num == target:
            print(comb + "R")
            break

        if new_num not in dic:
            dic[new_num] = 1
            queue.append([new_num, comb+"R"])