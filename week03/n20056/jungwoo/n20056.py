import sys
from typing import *

directions = [
    [-1, 0],
    [-1, 1],
    [0, 1],
    [1, 1],
    [1, 0],
    [1, -1],
    [0, -1],
    [-1, -1],
]


def correct_range(x, maxi):
    ret = x % maxi
    return ret


class Fire:
    def __init__(self, r, c, m, s, d):
        self.r = r
        self.c = c
        self.m = m
        self.s = s
        self.d = d

    def move(self, r, c):
        self.r, self.c = r, c


class FireContainer:
    def __init__(self):
        self.container = set()
        self.align = -1

    def add(self, fire: Fire):
        self.container.add(fire)

    def remove(self, fire):
        self.container.remove(fire)

    def add_multiple(self, fires: Set[Fire]):
        self.container.update(fires)

    def clear(self):
        self.container.clear()

    def do_align(self):
        self.align = -1
        for fire in self.container:
            self.__set_align(fire)
            if self.align == 2:
                break

    def is_align(self):
        self.do_align()
        return self.align != 2

    def size(self):
        return len(self.container)

    def __set_align(self, fire):
        if self.align == -1:
            self.align = fire.d % 2
        elif self.align == 2:
            pass
        elif self.align != fire.d % 2:
            self.align = 2


def move(arr, fires, n):
    for fire in fires:
        i, j = fire.r, fire.c
        i1, j1 = map(lambda x: x * fire.s, directions[fire.d])
        i2, j2 = (i + i1) % n, (j + j1) % n
        arr[i][j].remove(fire)
        arr[i2][j2].add(fire)
        fire.move(i2, j2)


def act(arr, new_arr, fires):
    new_fires = []
    for fire in fires:
        i, j = fire.r, fire.c
        if arr[i][j].size() == 0:
            continue
        if arr[i][j].size() == 1:
            new_arr[i][j].add(fire)
            new_fires.append(fire)
            arr[i][j].clear()
        else:
            m, s = 0, 0
            for fire2 in arr[i][j].container:
                m += fire2.m
                s += fire2.s
            m = int(m / 5)
            if m != 0:
                s = int(s / arr[i][j].size())
                ds = [0, 2, 4, 6] if arr[i][j].is_align() else [1, 3, 5, 7]
                for d in ds:
                    new_fire = Fire(i, j, m, s, d)
                    new_arr[i][j].add(new_fire)
                    new_fires.append(new_fire)
            arr[i][j].clear()
    return new_arr, arr, new_fires


def solution():
    input1 = sys.stdin.readline
    n, m, k = map(int, input1().split())
    arr = [[FireContainer() for _ in range(n)] for _ in range(n)]
    new_arr = [[FireContainer() for _ in range(len(arr))] for _ in range(len(arr))]
    fires = []
    for _ in range(m):
        f = Fire(*map(int, input1().split()))
        f.r -= 1
        f.c -= 1
        arr[f.r][f.c].add(f)
        fires.append(f)

    for i in range(k):
        move(arr, fires, n)
        arr, new_arr, fires = act(arr, new_arr, fires)
        if len(fires) == 0:
            break

    total = 0
    for f in fires:
        total += f.m
    print(total)


if __name__ == "__main__":
    solution()
