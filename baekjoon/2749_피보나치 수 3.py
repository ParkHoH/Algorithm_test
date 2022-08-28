# 피보나치의 주기: 15 * 10^(k-1)
# 주기의 길이가 P 이면, N번째 피보나치 수를 M으로 나눈 나머지는 N%P번째 피보나치 수를 M을 나눈 나머지와 같음

N = int(input())
fibo = [0, 1]

for i in range(2, 1500000):
    fibo.append(fibo[i-1] + fibo[i-2])
    fibo[i] %= 1000000

print(fibo[N%1500000])