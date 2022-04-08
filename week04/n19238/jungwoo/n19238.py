from collections import deque
from sys import stdin
from typing import Any

input = stdin.readline

DELTA = (
    (-1, 0),  # 상
    (0, -1),  # 좌
    (1, 0),  # 하
    (0, 1),  # 우
)


def is_in_range(n, a, b):
    return 0 <= a < n and 0 <= b < n


class OilEmptyException(Exception):
    pass


class White:
    def __init__(self, r, c, oil):
        self.r, self.c, self.oil = r, c, oil

    def change_position(self, pr, pc, distance):
        self.r, self.c, self.oil = pr, pc, self.oil + distance


class TaxiService:
    def __init__(self, white: White, arr):
        self.white = white
        self.arr, self.n = arr, len(arr)

    def find_nearby_passenger(self):
        w = self.white
        if isinstance(self.arr[w.r][w.c], tuple):
            return w.r, w.c, 0
        q = deque([[(w.r, w.c)]])
        visit = [[False] * self.n for _ in range(self.n)]
        visit[w.r][w.c] = True
        candidate_positions = []
        move_cnt = 0
        while move_cnt < self.white.oil and q:
            move_cnt += 1
            next_move_positions = []
            for r, c in q.popleft():
                for i in range(4):
                    x, y = DELTA[i][0] + r, DELTA[i][1] + c
                    if not is_in_range(self.n, x, y) or visit[x][y]:
                        continue
                    visit[x][y] = True
                    if isinstance(self.arr[x][y], tuple):
                        candidate_positions.append((x, y))
                    elif self.arr[x][y] == 0:
                        next_move_positions.append((x, y))
            if candidate_positions:
                return *min(candidate_positions), move_cnt
            elif next_move_positions:
                q.append(next_move_positions)
        raise OilEmptyException()

    def move_to_passenger(self, pr, pc, distance):
        self.white.change_position(pr, pc, distance)
        result = self.arr[pr][pc][:]
        self.arr[pr][pc] = 0
        return result

    def deliver_passenger(self, dr, dc):
        w = self.white
        q: deque = deque([[(w.r, w.c)]])
        visit = [[False] * self.n for _ in range(self.n)]
        visit[w.r][w.c] = True
        move_cnt = 0
        while move_cnt < self.white.oil and q:
            move_cnt += 1
            next_move_positions = []
            for r, c in q.popleft():
                for i in range(4):
                    x, y = DELTA[i][0] + r, DELTA[i][1] + c
                    if not is_in_range(self.n, x, y) or visit[x][y]:
                        continue
                    visit[x][y] = True
                    if x == dr and y == dc:
                        return move_cnt
                    if not (isinstance(self.arr[x][y], int) and self.arr[x][y] == 1):
                        next_move_positions.append((x, y))
            if next_move_positions:
                q.append(next_move_positions)
        raise OilEmptyException()

    def move_to_destination(self, dr, dc, distance):
        self.white.change_position(dr, dc, distance)


def solution():
    n, m, oil = map(int, input().split())
    arr: list[list[Any]] = [list(map(int, input().split())) for _ in range(n)]
    white = White(*map(lambda _x: int(_x) - 1, input().split()), oil)
    passengers: list[list[int]] = [list(map(lambda _x: int(_x) - 1, input().split())) for _ in range(m)]

    for p in passengers:
        arr[p[0]][p[1]] = (p[2], p[3])

    taxi_service = TaxiService(white, arr)

    try:
        for _ in range(len(passengers)):
            # Search nearby passenger
            pr, pc, pickup_distance = taxi_service.find_nearby_passenger()

            # Move white to passenger's position
            dr, dc = taxi_service.move_to_passenger(pr, pc, -pickup_distance)

            # Search delivery path
            deliver_distance = taxi_service.deliver_passenger(dr, dc)

            # Move white to destination
            taxi_service.move_to_destination(dr, dc, deliver_distance)
    except OilEmptyException:
        print(-1)
    else:
        print(taxi_service.white.oil)


if __name__ == "__main__":
    solution()
