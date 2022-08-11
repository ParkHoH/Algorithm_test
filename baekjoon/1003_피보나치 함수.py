T = int(input())
fibo = [[1, 0], [0, 1]]
for _ in range(39):
    zero = fibo[-1][0] + fibo[-2][0]
    one = fibo[-1][1] + fibo[-2][1]
    fibo.append([zero, one])

for _ in range(T):
    idx = int(input())
    print(fibo[idx][0], end=" ")
    print(fibo[idx][1])