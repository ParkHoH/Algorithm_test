def solution(m, musicinfos):
    dic_replace = {
        'C#': 'c',
        'D#': 'd',
        'F#': 'f',
        'G#': 'g',
        'A#': 'a'
    }
    new_musicinfos = [[] for _ in range(len(musicinfos))]
    
    for i in range(len(musicinfos)):
        musicinfos[i] = musicinfos[i].split(',')
        h_start, m_start = list(map(int, musicinfos[i][0].split(':')))
        h_end, m_end = list(map(int, musicinfos[i][1].split(':')))
        only_minute = (h_end-h_start)*60 + (m_end-m_start)
        new_musicinfos[i].append(only_minute)
        
        new_musicinfos[i].append(musicinfos[i][2])
        new_musicinfos[i].append(musicinfos[i][3])

        s = musicinfos[i][3]
        for key, value in dic_replace.items():
            s = s.replace(key, value)
        if len(s) > new_musicinfos[i][0]:
            new_musicinfos[i].append(s[:new_musicinfos[i][0]])
            new_musicinfos[i].append(s[:new_musicinfos[i][0]])
        else:
            new_musicinfos[i].append(s)
            new_musicinfos[i].append(s)

        while len(new_musicinfos[i][4]) < new_musicinfos[i][0]:
            new_musicinfos[i][4] += new_musicinfos[i][3]

    for key, value in dic_replace.items():
        if key in m:
            m = m.replace(key, value)

    result = []
    max_play = 0
    for new_musicinfo in new_musicinfos:
        if m in new_musicinfo[4]:
            result.append(new_musicinfo)
            max_play = max(max_play, result[-1][0])

    for i in range(len(result)):
        if result[i][0] == max_play:
            return result[i][1]
    return '(None)'


print(solution("CDEFGAC", ["12:00,12:06,HELLO,CDEFGA"]))
print(solution("CC#BCC#BCC#BCC#B",["03:00,03:30,FOO,CC#B", "04:00,04:08,BAR,CC#BCC#BCC#B"]))