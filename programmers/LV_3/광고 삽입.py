def time_to_seconds(time):
    time = time.split(":")
    time = int(time[0]) * 3600 + int(time[1]) * 60 + int(time[2])
    return time

def solution(play_time, adv_time, logs):
    play_time = time_to_seconds(play_time)
    adv_time = time_to_seconds(adv_time)
    all_time = [0] * (play_time+1)
    for i, log in enumerate(logs):
        start, end = log.split("-")
        start, end = time_to_seconds(start), time_to_seconds(end)
        logs[i] = [start, end]
        all_time[start] += 1
        all_time[end] -= 1

    for i in range(1, len(all_time)):
        all_time[i] += all_time[i-1]
    for i in range(1, len(all_time)):
        all_time[i] += all_time[i-1]
    
    most_view = 0
    time = 0                          
    for i in range(adv_time-1, play_time):
        if i >= adv_time:
            if most_view < all_time[i] - all_time[i - adv_time]:
                most_view = all_time[i] - all_time[i - adv_time]
                time = i - adv_time + 1
        else:
            if most_view < all_time[i]:
                most_view = all_time[i]
                time = i - adv_time + 1

    time = str(time // 3600).rjust(2, "0") + ":" + str(time % 3600 // 60).rjust(2, "0") + ":" + str(time % 3600 % 60).rjust(2, "0")
    return time