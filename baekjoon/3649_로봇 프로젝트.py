import sys
input = sys.stdin.readline

def binary_search(L, target_num):
    left = 0
    right = len(L) - 1
    
    while(left <= right):
        middle = (left + right) // 2
        if target_num < L[middle]:
            right = middle - 1
        elif L[middle] < target_num:
            left = middle + 1
        else:
            return middle
    return -1

while True:
    try:
        x = int(input()) * 10000000
        n = int(input())
        L = []

        for _ in range(n):
            L.append(int(input()))

        L.sort()
        possible = False

        for i in range(n):
            if L[i] > x // 2:
                break

            target_num = x - L[i]
            idx = binary_search(L, target_num)
            if idx != -1:
                possible = True
                break
        
        if possible:
            print(f"yes {L[i]} {L[idx]}")
        else:
            print("danger")

    except:
        break

# 정답
import sys
input = sys.stdin.readline

while True:
    try:
        x = int(input()) * 10000000
        n = int(input())
        L = []

        for _ in range(n):
            L.append(int(input()))

        L.sort()
        left = 0
        right = n-1
        possible = False

        while left < right:
            if L[left] + L[right] == x:
                possible = True
                break

            elif L[left] + L[right] > x:
                right -= 1
            else:
                left += 1

        if possible:
            print(f"yes {L[left]} {L[right]}")
        else:
            print("danger")

    except:
        break
