n = int(input())
prime = set(range(2, n+1))
for i in range(2, n+1):
    for j in range(2*i, n+1, i):
        if j in prime:
            prime.remove(j)
prime = list(prime)

answer = 0
start = end = 0
sum_prime = 0
while end < len(prime):
    sum_prime += prime[end]
    if sum_prime == n:
        answer += 1
    elif sum_prime > n:
        while start <= end:
            if sum_prime - prime[start] == n:
                answer += 1
                break
            elif sum_prime - prime[start] < n:
                break
            sum_prime -= prime[start]
            start += 1
    end += 1

print(answer)