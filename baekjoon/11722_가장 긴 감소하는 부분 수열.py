N = int(input())
A = list(map(int, input().split()))
dp = [-1] * (N)

def dfs(idx):
    if dp[idx] == -1:
        dp[idx] = 1

        for i in range(idx+1, N):
            if A[i] < A[idx]:
                dp[idx] = max(dp[idx], dfs(i)+1)

    return dp[idx]

for i in range(N):
    dfs(i)
    
print(max(dp))