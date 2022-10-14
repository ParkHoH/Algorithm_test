dice = {}
dice[1] = {
    "cur": 0,
    "left": 4,
    "right": 3,
    "up": 2,
    "down": 5
}

dice[2] = {
    "cur": 0,
    "left": 4,
    "right": 3,
    "up": 2,
    "down": 5
}

dice[3] = {
    "cur": 0,
    "left": 1,
    "right": 6,
    "up": 2,
    "down": 5
}

dice[4] = {
    "cur": 0,
    "left": 6,
    "right": 1,
    "up": 2,
    "down": 5
}

N, M, dice_x, dice_y, K = map(int, input().split()) 
board = [list(map(int, input().split())) for _ in range(N)]
orders = list(map(int, input().split()))