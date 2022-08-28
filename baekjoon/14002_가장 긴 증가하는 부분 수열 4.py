N = int(input())
L = list(map(int, input().split()))
dp = [-1] * N

def dfs(idx):
    if dp[idx] == -1:
        dp[idx] = [L[idx]]

        for i in range(idx+1, N):
            if L[idx] < L[i]:
                new_list = [L[idx]] + dfs(i)
                if len(dp[idx]) < len(new_list):
                    dp[idx] = new_list

    return dp[idx]

for i in range(N):
    if dp[i] == -1:
        dfs(i)

max_len = max_idx = 0
for i in range(N):
    if max_len < len(dp[i]):
        max_len = len(dp[i])
        max_idx = i

print(max_len)
print(*dp[max_idx])