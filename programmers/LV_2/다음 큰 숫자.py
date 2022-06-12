def solution(n):
    cnt = bin(n)[2:].count("1")
    
    while n <= 1000001:
        n += 1
        if bin(n)[2:].count("1") == cnt:
            return n

print(solution(15))

# other solution
def change_num(n):
    s = ''
    while n:
        s += str(n % 2)
        n //= 2
    return s[::-1]

def solution(n):
    num = change_num(n).count("1")
    i = n + 1
    while True:
        if change_num(i).count("1") == num:
            return i
        i += 1