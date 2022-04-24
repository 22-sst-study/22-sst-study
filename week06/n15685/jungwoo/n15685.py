from sys import stdin

input1 = stdin.readline
directions = (
    (0, 1),  # 우
    (-1, 0),  # 상
    (0, -1),  # 좌
    (1, 0),  # 하
)


def is_in_range(obj, a, b):
    if isinstance(obj, int):
        return 0 <= a < obj and 0 <= b < obj
    else:
        return 0 <= a < len(obj) and 0 <= b < len(obj)


def dragon(dot, dot_set, r, c, d, g, prev, history):
    if g == 0:
        return
    cr, cc, cd = r, c, d
    for pd in prev:
        x, y = directions[(cd + pd) % 4][0] + cr, directions[(cd + pd) % 4][1] + cc
        dot[x][y] = 1
        dot_set.add((x, y))
        cr, cc, cd = x, y, (cd + pd) % 4
    curr = [-prev[len(prev)-i-1] for i in range(len(prev))]
    new_history = curr + history
    dragon(dot, dot_set, cr, cc, cd, g - 1, [1] + new_history, new_history)


def search(dot, dot_set):
    square = 0
    for r, c in dot_set:
        tmp = (r, c), (r, c+1), (r+1, c), (r+1, c+1)
        if all([is_in_range(len(dot), t[0], t[1]) and dot[t[0]][t[1]] for t in tmp]):
            square += 1
    return square


def solution():
    n = int(input())

    dot = [[0] * 101 for _ in range(101)]
    dot_set = set()

    for _ in range(n):
        c, r, d, g = map(int, input().split())
        x, y = directions[d][0] + r, directions[d][1] + c
        dot[r][c] = dot[x][y] = 1
        dot_set |= {(r, c), (x, y)}
        dragon(dot, dot_set, x, y, d, g, [1], [])

    print(search(dot, dot_set))


if __name__ == "__main__":
    solution()
