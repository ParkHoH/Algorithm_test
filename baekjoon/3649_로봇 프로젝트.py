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
