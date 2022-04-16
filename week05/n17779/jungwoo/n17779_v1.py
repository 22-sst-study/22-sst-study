import itertools
from collections import deque
from sys import stdin

input1 = stdin.readline
# directions = (
#     (-1, 0),  # 상
#     (0, -1),  # 좌
#     (1, 0),  # 하
#     (0, 1),  # 우
# )


# def is_in_range(obj, a, b):
#     if isinstance(obj, int):
#         return 0 <= a < obj and 0 <= b < obj
#     else:
#         return 0 <= a < len(obj) and 0 <= b < len(obj)


def search_rc(n, arr, area_checker, x, y, d1, d2):
    cnt = [0] * 5
    for i in range(n):
        for j in range(n):
            for area in range(len(area_checker)):
                if area_checker[area](i, j, x, y, d1, d2):
                    cnt[area] += arr[i][j]
                    break
    return cnt


def search_d1d2(n, arr, area_checker, x, y):
    min_diff = 2000
    for d1 in range(1, n - 1):
        for d2 in range(1, n - 1):  # n - 2 - 1
            if not (x+d1+d2 < n and 0 <= y-d1 < y < y+d2 < n):
                continue
            cnt = search_rc(n, arr, area_checker, x, y, d1, d2)
            min_diff = min(max(cnt) - min(cnt), min_diff)
    return min_diff


def search_xy(n, arr, area_checker):
    min_diff = 2000
    for i in range(1, n - 2):
        for j in range(1, n - 2):
            min_diff = min(search_d1d2(n, arr, area_checker, i, j), min_diff)
    return min_diff


def is_area5(r, c, x, y, d1, d2):
    a1, b1 = x, y
    a2, b2 = a1 + d1, b1 - d1
    a3, b3 = a2 + d2, b2 + d2
    a4, b4 = a3 - d1, b3 + d1

    if a1 <= r <= a2 and b2 <= c <= b1:
        diff = a1 - r
        if b1 + diff <= c:
            return True
    elif a2 <= r <= a3 and b2 <= c <= b3:
        diff = r - a2
        if b2 + diff <= c:
            return True
    elif a4 <= r <= a3 and b3 <= c <= b4:
        diff = a3 - r
        if c <= b3 + diff:
            return True
    elif a1 <= r <= a4 and b1 <= c <= b4:
        diff = r - a1
        if c <= b1 + diff:
            return True


def solution():
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

    area_checker = [
        lambda r, c, x, y, d1, d2: is_area5(r, c, x, y, d1, d2),
        lambda r, c, x, y, d1, d2: r < x + d1 and c <= y,
        lambda r, c, x, y, d1, d2: r <= x+d2 and y < c,
        lambda r, c, x, y, d1, d2: x+d1 <= r and c < y-d1+d2,
        lambda r, c, x, y, d1, d2: x+d2 < r and y-d1+d2 <= c,
    ]

    print(search_xy(n, arr, area_checker))


if __name__ == "__main__":
    solution()
