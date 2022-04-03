from sys import stdin

input1 = stdin.readline
directions = (
    (-1, 0),  # 상
    (0, -1),  # 좌
    (1, 0),  # 하
    (0, 1),  # 우
)
sd = (
    (-1, 0),  # 상
    (-1, -1),  # 상좌
    (0, -1),  # 좌
    (1, -1),  # 좌하
    (1, 0),  # 하
    (1, 1),  # 하우
    (0, 1),  # 우
    (-1, 1),  # 우상
)


def is_in_range(n, a, b):
    return 0 <= a < n and 0 <= b < n


def can_turn_left(visit, r, c, _d):
    d = (_d + 1) % 4
    x, y = directions[d][0] + r, directions[d][1] + c
    if not is_in_range(len(visit), x, y) or visit[x][y]:
        return False, -1, -1
    return True, x, y


def go_straight(r, c, d):
    return directions[d][0] + r, directions[d][1] + c


def stooooooorm(arr, r, c, d):
    n = len(arr)
    total = arr[r][c]
    arr[r][c] = 0
    moved_sand_amount, out_sand_amount = 0, 0

    # 5%
    t = total // 20
    x, y = r + sd[d][0] * 2, c + sd[d][1] * 2
    if is_in_range(n, x, y):
        arr[x][y] += t
    else:
        out_sand_amount += t
    moved_sand_amount += t

    # 10%
    t = total // 10
    for i in (1, -1):
        x, y = r + sd[(d + i) % 8][0], c + sd[(d + i) % 8][1]
        if is_in_range(n, x, y):
            arr[x][y] += t
        else:
            out_sand_amount += t
        moved_sand_amount += t

    # 7%
    t = int(total / 100 * 7)
    for i in (2, -2):
        x, y = r + sd[(d + i) % 8][0], c + sd[(d + i) % 8][1]
        if is_in_range(n, x, y):
            arr[x][y] += t
        else:
            out_sand_amount += t
        moved_sand_amount += t

    # 2%
    t = total // 50
    for i in (2, -2):
        x, y = r + sd[(d + i) % 8][0] * 2, c + sd[(d + i) % 8][1] * 2
        if is_in_range(n, x, y):
            arr[x][y] += t
        else:
            out_sand_amount += t
        moved_sand_amount += t

    # 1%
    t = total // 100
    for i in (3, -3):
        x, y = r + sd[(d + i) % 8][0], c + sd[(d + i) % 8][1]
        if is_in_range(n, x, y):
            arr[x][y] += t
        else:
            out_sand_amount += t
        moved_sand_amount += t

    # rest
    t = total - moved_sand_amount
    x, y = r + sd[d][0], c + sd[d][1]
    if is_in_range(n, x, y):
        arr[x][y] += t
    else:
        out_sand_amount += t

    return out_sand_amount


def solution():
    n = int(input1())
    arr = [list(map(int, input1().split())) for _ in range(n)]

    r, c, d = n // 2, n // 2, 0
    visit = [[False] * n for _ in range(n)]
    visit[r][c] = True
    out_sand_amount = 0
    for _ in range(n**2):
        # move
        turn, x, y = can_turn_left(visit, r, c, d)
        if turn:
            r, c, d = x, y, (d + 1) % 4
        else:
            r, c = go_straight(r, c, d)
        visit[r][c] = True

        # sand storm
        out_sand_amount += stooooooorm(arr, r, c, d * 2)

    print(out_sand_amount)


if __name__ == "__main__":
    solution()
