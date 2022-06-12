import sys
sys.setrecursionlimit(60000)

def solution(n):
    memory = [-1 for i in range(60001)]

    def dp(n):
        if memory[n] != -1: return memory[n]
        if n == 0: return 1
        if n == 1: return 1
        memory[n] = (dp(n-1) + dp(n-2)) % 1000000007
        return memory[n]

    return dp(n)