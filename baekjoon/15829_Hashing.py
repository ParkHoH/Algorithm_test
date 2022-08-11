L = int(input())
string = input()
sum = 0
idx = 0

for s in string:
    num = ord(s) - 96
    sum += num * (31 ** idx)
    idx += 1

print(sum % 1234567891)