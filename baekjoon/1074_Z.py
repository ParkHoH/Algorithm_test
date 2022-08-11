N, r, c = map(int, input().split())
num = 2 ** N // 2
a = (r // 2) * 4 * num
b = (c // 2) * 4
c = (r // 2) * 2
d = (c // 2)
print(a + b + c + d)