

# 시간 초과
def solution(k, room_number):
    room_available = set(range(1, k+1))
    occupied = [False] * (k+1)
    result = []
    for num in room_number:
        if occupied[num] == False:
            result.append(num)
            occupied[num] = True
            room_available.remove(num)
        else:
            for room in room_available:
                if room > num:
                    result.append(room)
                    occupied[room] = True
                    room_available.remove(room)
                    break
    return result


# 시간 초과
def solution(k, room_number):
    room = [False] * (k+1)
    result = []
    for num in room_number:
        if room[num] == False:
            result.append(num)
            room[num] = True
        else:
            i = num+1
            while True:
                if room[i] == False:
                    result.append(i)
                    room[i] = True
                    break
                i += 1
    return result