n = int(input())
arr = list(map(int, input().split()))

new_arr = []
sum = 0
if arr[0] >= 0:
    plus = True
else:
    plus = False

for i in arr:
    if i > 0 and plus:
        sum += i
        
    elif i > 0 and not plus:
        plus = True
        new_arr.append(sum)
        sum = i
    
    elif i < 0 and plus:
        plus = False
        new_arr.append(sum)
        sum = i

    elif i < 0 and not plus:
        sum += i

print(new_arr)