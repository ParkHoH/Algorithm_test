from itertools import permutations

def solution(user_id, banned_id):
    result = []
    for users in list(permutations(user_id, len(banned_id))):
        stop = False
        for user, ban_id in zip(users, banned_id):
            if len(user) != len(ban_id):
                stop = True
                break
            for i in range(len(user)):
                if ban_id[i] != "*" and user[i] != ban_id[i]:
                    stop = True
                    break
            if stop: break

        if not stop and set(users) not in result:
            result.append(set(users))
            
    return len(result)

print(solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"]))