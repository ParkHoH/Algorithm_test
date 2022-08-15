T = int(input())
for _ in range(T):
    M, N, x, y = map(int, input().split())
    result = -1

    while(x <= M*N):
        if x%N == y%N:
            result = x
            break
        x += M

    print(result)

# def find(a, b, m, n):
#     diff = n - m
#     cnt = b - 1
#     a_num = a - cnt
#     while a_num < 1:
#         a_num += m-1

#     if (a_num - 1) % diff == 0: # 가능한 경우
#         return (a_num - 1) // diff * (n-1) + cnt + 1
#     else:
#         return -1

# T = int(input())
# for _ in range(T):
#     M, N, x, y = map(int, input().split())
#     M += 1
#     N += 1

#     if N >= M:
#         print(find(x, y, M, N))
#     else:
#         print(find(y, x, N, M))
