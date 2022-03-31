# short solution
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x*3, reverse=True)
    return str(int(''.join(numbers)))


# my solution
def solution(numbers):  
    numbers = list(map(str, numbers))
    numbers.sort(reverse=True)
    i = 1
    while i <= len(numbers)-1:
        if i < 1: 
            i = 1
        if numbers[i] + numbers[i-1] > numbers[i-1] + numbers[i]:
            numbers[i], numbers[i-1] = numbers[i-1], numbers[i]
            i -= 2
        i += 1
    return str(int(''.join(numbers)))


# my solution_2: wrong
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(reverse=True)
    for i in range(len(numbers)-1, 0, -1):
        if numbers[i-1][:len(numbers[i])] == numbers[i]:
            if int(numbers[i-1] + numbers[i]) < int(numbers[i] + numbers[i-1]):
                numbers[i-1], numbers[i] = numbers[i], numbers[i-1]
    return ''.join(numbers)


# my solution: wrong
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(reverse=True)
    for i in range(len(numbers)-1, 0, -1):
        if numbers[i-1][:len(numbers[i])] == numbers[i]:
            change = False
            for j in range(len(numbers[i]), len(numbers[i-1])):
                if int(numbers[i-1][j]) < int(numbers[i][0]):
                    change = True
                    break
                elif int(numbers[i-1][j]) > int(numbers[i][0]):
                    change = False
                    break
            if change:
                numbers[i-1], numbers[i] = numbers[i], numbers[i-1]
    return ''.join(numbers)


print(solution([30, 33, 3, 34]))
print(solution([ 979, 97, 978, 81,818,817]))
print(solution([ 67,676,677,]))