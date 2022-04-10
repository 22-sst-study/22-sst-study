import copy
from sys import stdin

# input = stdin.readline
# directions = (
#     (-1, 0),  # 상
#     (0, -1),  # 좌
#     (1, 0),  # 하
#     (0, 1),  # 우
# )
directions = (
    (-1, 0),  # 상
    (-1, -1),  # 상좌
    (0, -1),  # 좌
    (1, -1),  # 좌하
    (1, 0),  # 하
    (1, 1),  # 하우
    (0, 1),  # 우
    (-1, 1),  # 우상
)
img = ['↑', '↖', '←', '↙', '↓', '↘', '→', '↗']


def is_in_range(n, a, b):
    return 0 <= a < n and 0 <= b < n


class Animal:
    def __init__(self, r, c, aid, d, alive=True):
        self.r, self.c, self.aid, self.d, self.alive = r, c, aid, d, alive

    def __repr__(self):  # for debug
        if self.alive != 'alive':
            return f'D{img[self.d]}'
        else:
            return f'{self.aid}{img[self.d]}'

    def __eq__(self, other):
        return self.r == other.r and self.c == other.c

    def get_next_pos(self, dist=1):
        return self.r + directions[self.d][0] * dist, self.c + directions[self.d][1] * dist

    def change_pos(self, r, c, d):
        self.r, self.c, self.d = r, c, d


class Shark(Animal):
    pass


class Fish(Animal):

    def __init__(self, r, c, aid, d):
        super().__init__(r, c, aid, d)

    def ate(self):
        self.alive = False
        return self.aid + 1, self.r, self.c, self.d

    @staticmethod
    def move(arr, fish, shark):
        for f in fish:
            if f == shark or not f.alive:
                continue
            x, y = f.move()
            while not is_in_range(4, x, y) or (x == shark.r and y == shark.c):
                f.d = (f.d + 1) % 8
                x, y = f.move()
            f.swap(arr, fish, x, y)

    def swap(self, arr, fish, x, y):
        other = fish[arr[x][y]]
        arr[x][y], arr[self.r][self.c] = arr[self.r][self.c], arr[x][y]
        self.r, self.c, other.r, other.c = other.r, other.c, self.r, self.c


def start(arr: list[list[int]], fish, shark, total):
    Fish.move(arr, fish, shark)
    ret = [total]
    for i in range(1, 4):
        x, y = shark.move(i)
        if not is_in_range(4, x, y):
            break
        f = fish[arr[x][y]]
        if f.alive:
            new_arr, new_fish, new_shark = copy.deepcopy(arr), copy.deepcopy(fish), copy.deepcopy(shark)
            aid, r, c, d = new_fish[f.aid].ate()
            new_shark.change_pos(r, c, d)
            ret.append(start(new_arr, new_fish, new_shark, total + aid))
    return max(ret)


def solution():
    arr, fish = [], []
    shark = Shark(0, 0, 0, -1)
    for r in range(4):
        _tmp = list(map(int, input().split()))
        _arr = [Fish(r, c, i - 1, j - 1) for c, i, j in zip(range(4), _tmp[0::2], _tmp[1::2])]
        arr.append(list(map(lambda _x: _x.aid, _arr)))
        fish += _arr

    first = fish[0]
    aid, r, c, d = first.ate()
    shark.change_pos(r, c, d)
    fish.sort(key=lambda _x: _x.aid)
    print(start(arr, fish, shark, aid))


if __name__ == "__main__":
    solution()
