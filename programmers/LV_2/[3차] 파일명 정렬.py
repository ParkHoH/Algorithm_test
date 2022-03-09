import re

def solution(files):
    p = re.compile('([a-zA-Z\s.-]+)([0-9]{1,5})([a-zA-Z0-9\s.-]*)')
    result = [0] * len(files)
    for i in range(len(files)):
        result[i] = p.findall(files[i])
        result[i] = [result[i][0], result[i][0][0].lower(), re.sub('^[0]*', '', result[i][0][1])]
        result[i][2] = '0' if result[i][2] == '' else result[i][2]  #위 re.sub에 대한 예외처리(빈 문자열을 밑에서 int로 변경하면 오류 발생)
    result.sort(key=lambda x: (x[1], int(x[2])))
    return [''.join(item[0]) for item in result]


#better soluton
def solution(files):
    result = [re.findall('(\D+)([0-9]{1,5})(.*)', file)[0] for file in files]
    result.sort(key=lambda x: (x[0].upper(), int(x[1])))
    return [''.join(item) for item in result]


print(solution(["O00321", "O49qcGPHuRLR5FEfoO00321"]))