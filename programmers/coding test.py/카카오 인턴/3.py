def solution(alp, cop, problems):
    required_alp = required_cop = 0
    for problem in problems:
        required_alp = max(required_alp, problem[0])
        required_cop = max(required_cop, problem[1])