from collections import deque

def solution(arr, processes):
    count = 0
    for i in range(len(processes)):
        processes[i] = processes[i].split()
        if processes[i][0] == "read":
            count += 1

    process_queue = []
    read_wait = deque()
    write_wait = deque()
    result = [0 for _ in range(count+1)]
    cnt = 0
    used_time = 0
    count = 0
    for process in processes:
        cnt += 1
        used_time += 1
        if process[0] == "read":
            read_wait.append(process + [count])
            count += 1
        else:
            write_wait.append(process)

        # 작업 중인 프로세스가 없을 경우
        if len(process_queue) == 0:
            # wirte 프로세스가 대기 중일 경우
            if len(write_wait) != 0 and int(write_wait[0][1]) <= cnt:
                process = write_wait.popleft()
                process[2] = str(int(process[2]) + cnt)
                process_queue.append(process)
            
            # 대기 중인 write 프로세스가 없을 경우
            else:
                while (len(read_wait) > 0) and (int(read_wait[0][1]) <= cnt):
                    process = read_wait.popleft()
                    process[2] = str(int(process[2]) + cnt)
                    process_queue.append(process)
                    if len(read_wait) == 0:
                        break

        # 작업 중인 프로세스가 있을 경우
        # 작업 중인 프로세스가 read인 경우만
        if len(process_queue) > 0 and process_queue[0][0] == "read" and len(write_wait) == 0:
            # 대기 중인 read 프로세스 모두 작업 프로세스에 넣어주기
            while (len(read_wait) > 0) and (int(read_wait[0][1]) <= cnt):
                process = read_wait.popleft()
                process[2] = str(int(process[2]) + cnt)
                process_queue.append(process)
                if len(read_wait) == 0:
                        break

        if len(process_queue) == 0:
            used_time -= 1

        # 작업 완료됐나 체크
        for i in range(len(process_queue)-1 , -1, -1):
            if int(process_queue[i][2]) == cnt+1:
                complited_process = process_queue.pop(i)
                start = int(complited_process[3])
                end = int(complited_process[4]) + 1
                # read일 경우
                if complited_process[0] == "read":
                    result[complited_process[5]] = ''.join(arr[start:end])
                # write일 경우
                else:
                    arr = [arr[i] for i in range(start)] + [complited_process[5] for _ in range(end-start)] + [arr[i] for i in range(end, len(arr))]

    while len(read_wait) != 0 or len(process_queue) != 0 or len(write_wait) != 0:
        cnt += 1
        used_time += 1
        # 작업 중인 프로세스가 없을 경우
        if len(process_queue) == 0:
            # wirte 프로세스가 대기 중일 경우
            if len(write_wait) != 0 and int(write_wait[0][1]) <= cnt:
                process = write_wait.popleft()
                process[2] = str(int(process[2]) + cnt)
                process_queue.append(process)
            
            # 대기 중인 write 프로세스가 없을 경우
            else:
                while (len(read_wait) > 0) and (int(read_wait[0][1]) <= cnt):
                    process = read_wait.popleft()
                    process[2] = str(int(process[2]) + cnt)
                    process_queue.append(process)
                    if len(read_wait) == 0:
                        break

        # 작업 중인 프로세스가 있을 경우
        # 작업 중인 프로세스가 read인 경우만
        if len(process_queue) > 0 and process_queue[0][0] == "read" and len(write_wait) == 0:
            # 대기 중인 read 프로세스 모두 작업 프로세스에 넣어주기
            while (len(read_wait) > 0) and (int(read_wait[0][1]) <= cnt):
                process = read_wait.popleft()
                process[2] = str(int(process[2]) + cnt)
                process_queue.append(process)
                if len(read_wait) == 0:
                        break

        if len(process_queue) == 0:
            used_time -= 1

        # 작업 완료됐나 체크
        for i in range(len(process_queue)-1 , -1, -1):
            if int(process_queue[i][2]) == cnt+1:
                complited_process = process_queue.pop(i)
                start = int(complited_process[3])
                end = int(complited_process[4]) + 1
                # read일 경우
                if complited_process[0] == "read":
                    result[complited_process[5]] = ''.join(arr[start:end])
                # write일 경우
                else:
                    arr = [arr[i] for i in range(start)] + [complited_process[5] for _ in range(end-start)] + [arr[i] for i in range(end, len(arr))]
    result[-1] = str(used_time)
    return result
            

print(solution(["1","1","1","1","1","1","1"],["write 1 12 1 5 8","read 2 3 0 2","read 5 5 1 2","read 7 5 2 5","write 13 4 0 1 3","write 19 3 3 5 5","read 30 4 0 6","read 32 3 1 5"]))
print(solution(["1","2","4","3","3","4","1","5"],["read 1 3 1 2","read 2 6 4 7","write 4 3 3 5 2","read 5 2 2 5","write 6 1 3 3 9", "read 9 1 0 7"]))