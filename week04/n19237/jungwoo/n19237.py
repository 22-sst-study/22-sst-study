import copy
from sys import stdin

# input = stdin.readline
from typing import Any

directions = (
    (-1, 0),  # 상
    (0, -1),  # 좌
    (1, 0),  # 하
    (0, 1),  # 우
)


def change_direction(d):
    if d == 1:
        return 0
    elif d == 2:
        return 2
    elif d == 3:
        return 1
    else:
        return 3


def is_in_range(n, a, b):
    return 0 <= a < n and 0 <= b < n


class Shark:

    def __init__(self, arr: list[list[list[int]]], sid, r, c, d, k, move_orders):
        self.arr, self.sid, self.r, self.c, self.d, self.k = arr, sid, r, c, d, k
        self.move_orders = move_orders

    def move(self, x, y, m, now):
        if self.arr[x][y][1] == now + self.k and 0 < self.arr[x][y][0] < self.sid:
            return False
        else:
            self.change_status(x, y, m, now)
            return True

    def get_next_pos(self, now):
        for run_time in range(2):
            for m in self.move_orders[self.d]:
                x, y = self.r + directions[m][0], self.c + directions[m][1]
                if not is_in_range(len(self.arr[0]), x, y):
                    continue
                if self.arr[x][y][1] < now or (run_time == 1 and self.arr[x][y][0] == self.sid):
                    return x, y, m

    def change_status(self, x, y, m, now):
        self.r, self.c, self.d = x, y, m
        self.arr[self.r][self.c] = [self.sid, now + self.k]


def solution():
    n, m, k = map(int, input().split())
    arr = [list(map(lambda _x: [int(_x), 0], input().split())) for _ in range(n)]
    sd = list(map(lambda _x: change_direction(int(_x)), input().split()))
    shark_orders = {}
    for i in range(m):
        shark_order = [list(map(lambda _x: change_direction(int(_x)), input().split())) for _ in range(4)]
        shark_order[1], shark_order[2] = shark_order[2], shark_order[1]
        shark_orders[i] = shark_order
    sharks: list[Shark] = [Any] * m
    for i in range(n):
        for j in range(n):
            if arr[i][j][0] > 0:
                sid = arr[i][j][0]
                sharks[sid - 1] = Shark(arr, sid, i, j, sd[sid - 1], k, shark_orders[sid - 1])
                arr[i][j][1] = k

    banned = set()
    for t in range(1, 1001):
        move_candidate_positions = [Any] * m
        for i in range(m):
            if i in banned:
                continue
            move_candidate_positions[i] = sharks[i].get_next_pos(t)
        for i in range(m):
            if i in banned:
                continue
            x, y, d = move_candidate_positions[i]
            if not sharks[i].move(x, y, d, t):
                banned.add(i)
        if len(banned) == m - 1:
            print(t)
            return
    print(-1)


if __name__ == "__main__":
    solution()
