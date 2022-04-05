# from sys import stdin
#
# input1 = stdin.readline
directions = (
    (-1, 0),  # 상
    (0, -1),  # 좌
    (1, 0),  # 하
    (0, 1),  # 우
)


def get_d(d):
    if d == 1:
        return 3
    elif d == 2:
        return 1
    elif d == 3:
        return 0
    else:
        return 2


class Mal:

    change_cmds = [lambda _x1: reversed(_x1), lambda _x2: _x2]

    def __init__(self, arr, mal_arr, mid, r, c, d):
        self.arr, self.mal_arr, self.mid, self.r, self.c, self.d = arr, mal_arr, mid, r, c, get_d(d)
        self.mal_arr[r][c].append(self)

    def __repr__(self):
        return str(self.mid)

    def is_full(self):
        return len(self.mal_arr[self.r][self.c]) >= 4

    def move(self):
        can_move, x, y = self._get_next_pos()
        if can_move:
            self._change_pos(x, y)

    def _get_next_pos(self):
        x, y = directions[self.d][0] + self.r, directions[self.d][1] + self.c
        if self.arr[x][y] == 2:
            self.d = (self.d + 2) % 4
            x, y = directions[self.d][0] + self.r, directions[self.d][1] + self.c
            if self.arr[x][y] == 2:
                return False, -1, -1
        return True, x, y

    def _change_pos(self, x, y):
        popped: list[Mal] = [self.mal_arr[self.r][self.c].pop()]
        while len(self.mal_arr[self.r][self.c]) and popped[-1] is not self:
            popped.append(self.mal_arr[self.r][self.c].pop())
        for mal in popped:
            mal._set_pos(x, y)
        self.mal_arr[x][y].extend(self.change_cmds[self.arr[x][y]](popped))

    def _set_pos(self, x, y):
        self.r, self.c = x, y


def solution():
    n, k = map(int, input().split())
    arr = [list(map(int, f'2 {input()} 2'.split())) for _ in range(n)]
    arr.insert(0, [2] * (n + 2))
    arr.append([2] * (n + 2))
    mal_container = []
    mal_arr = [[[] for _ in range(n + 2)] for _ in range(n + 2)]
    for i in range(k):
        mal = Mal(arr, mal_arr, i + 1, *map(int, input().split()))
        mal_container.append(mal)

    for i in range(1, 1001):
        for mal in mal_container:
            mal.move()
            if mal.is_full():
                print(i)
                return
    print(-1)


if __name__ == "__main__":
    solution()
