from sys import stdin

input1 = stdin.readline
directions = (
    (0, 1),  # 우
    (1, 0),  # 하
    (0, -1),  # 좌
    (-1, 0),  # 상
)


def is_in_range(n, a, b):
    return 0 <= a < n and 0 <= b < n


class Context:
    def __init__(self, arr, likes):
        self.arr, self.likes, self.like_cnt, self.empty_cnt, self.r, self.c = arr, likes, -1, -1, 0, 0

    def set_new_pos(self, i, j):
        like_cnt, empty_cnt = 0, 0
        for d in range(4):
            x, y = directions[d][0] + i, directions[d][1] + j
            if not is_in_range(len(self.arr), x, y):
                continue
            if self.arr[x][y] in self.likes:
                like_cnt += 1
            elif self.arr[x][y] == 0:
                empty_cnt += 1
        if self.like_cnt < like_cnt:
            self._update(like_cnt, empty_cnt, i, j)
        elif self.like_cnt == like_cnt and self.empty_cnt < empty_cnt:
            self._update(like_cnt, empty_cnt, i, j)

    def _update(self, like_cnt, empty_cnt, r, c):
        self.like_cnt, self.empty_cnt, self.r, self.c = like_cnt, empty_cnt, r, c


def get_sit(arr, likes):
    context = Context(arr, likes)
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] == 0:
                context.set_new_pos(i, j)
    return context.r, context.c


def get_satisfaction(arr, likes_dic):
    total = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            cnt = 0
            for k in range(4):
                x, y = directions[k][0] + i, directions[k][1] + j
                if not is_in_range(len(arr), x, y):
                    continue
                if arr[x][y] in likes_dic[arr[i][j]]:
                    cnt += 1
            if cnt:
                total += 10 ** (cnt - 1)
    return total


def solution():
    n = int(input1())
    likes_dic = {}
    for _ in range(n ** 2):
        _s, *_likes = map(int, input1().split())
        likes_dic[_s] = set(_likes)
    
    arr = [[0] * n for _ in range(n)]
    for s, likes in likes_dic.items():
        r, c = get_sit(arr, likes)
        arr[r][c] = s

    print(get_satisfaction(arr, likes_dic))


if __name__ == "__main__":
    solution()
