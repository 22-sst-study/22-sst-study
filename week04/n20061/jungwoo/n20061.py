from sys import stdin

input = stdin.readline

DELTA = (
    (-1, 0),  # 상
    (0, -1),  # 좌
    (1, 0),  # 하
    (0, 1),  # 우
)


def is_in_range(n, a, b):
    return 0 <= a < n and 0 <= b < n


def process(brd, rs, cs):
    for i in range(6 - len(rs)):
        if not is_empty(brd, rs, cs, i):
            return insert(brd, rs, cs, i)
    return insert(brd, rs, cs, 6 - len(rs))


def is_empty(green, rs, cs, i):
    for r in range(i, len(rs) + i):
        for c in cs:
            if green[r + 1][c] == 1:
                return False
    return True


def insert(brd, rs, cs, i):
    real_rs, real_cs = [], []
    for r in range(i, len(rs) + i):
        for c in cs:
            brd[r][c] = 1
            real_rs.append(r)
            real_cs.append(c)
    return tuple(real_rs), tuple(real_cs)


def get_positions_for_green(t, r, c):
    if t == 1:
        return (r,), (c,)
    elif t == 2:
        return (r,), (c, c + 1)
    else:
        return (r, r + 1), (c,)


def get_positions_for_blue(t, r, c):
    if t == 1:
        return (c,), (r,)
    elif t == 2:
        return (c, c + 1), (r,)
    else:
        return (c,), (r, r + 1)


def remove(brd):
    new_brd = []
    for i in range(6):
        if not all(brd[i]):
            new_brd.append(brd[i])
    point = 6 - len(new_brd)
    if point:
        new_brd = [[0, 0, 0, 0] for _ in range(point)] + new_brd
    out_cnt = int(any(new_brd[0])) + int(any(new_brd[1]))
    if out_cnt:
        new_brd = [[0, 0, 0, 0] for _ in range(out_cnt)] + new_brd[:-out_cnt]
    return new_brd, point


def solution():
    n = int(input())
    inputs = [list(map(int, input().split())) for _ in range(n)]
    green = [[0, 0, 0, 0] for _ in range(6)]
    blue = [[0, 0, 0, 0] for _ in range(6)]

    point = 0
    for t, r, c in inputs:
        rs, cs = get_positions_for_green(t, r, c)
        process(green, rs, cs)
        rs, cs = get_positions_for_blue(t, r, c)
        process(blue, rs, cs)

        green, _point = remove(green)
        point += _point
        blue, _point = remove(blue)
        point += _point
    print(point)
    print(sum([sum(a) for a in green]) + sum([sum(a) for a in blue]))


if __name__ == "__main__":
    solution()
