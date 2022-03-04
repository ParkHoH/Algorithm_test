#my solution
def solution(phone_number):
    
    new_num = '*' * (len(phone_number) - 4)
    for i in range(len(phone_number)-4, len(phone_number)):
        new_num += phone_number[i]
    
    return new_num

#better solution
def solution(phone_number):
    
    new_num = '*' * (len(phone_number) - 4) + phone_number[-4:]
    
    return new_num
