S = input()
for i in range(len(S)):
    new_s = S + S[:i][::-1]
    center = len(new_s) // 2
    s_1 = new_s[:center]
    s_2 = new_s[center+1:][::-1] if len(new_s) % 2 else new_s[center:][::-1]
    if s_1 == s_2:
        print(len(new_s))
        break