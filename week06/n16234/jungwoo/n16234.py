from collections import deque
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


class Context:
    def __init__(self, arr, visit, r, c):
        self.arr, self.visit, self.r, self.c = arr, visit, r, c
        self.population = arr[r][c]
        self.positions = [(r, c)]
        self.visit[r][c] = True

    def __repr__(self):
        return str(self.positions)

    def visit_func(self, x, y):
        self.visit[x][y] = True
        self.population += self.arr[x][y]
        self.positions.append((x, y))


def bfs(arr, visit, _r, _c, l1, r1) -> Context:
    context = Context(arr, visit, _r, _c)
    q = deque([[(_r, _c)]])
    while q:
        popped = q.popleft()
        next_pos = []
        for r, c in popped:
            for a, b in directions:
                x, y = a + r, b + c
                if not is_in_range(len(arr), x, y) or visit[x][y]:
                    continue
                if l1 <= abs(arr[x][y] - arr[r][c]) <= r1:
                    next_pos.append((x, y))
                    context.visit_func(x, y)
        if next_pos:
            q.append(next_pos)
    return context


def move(context: Context, new_candidates):
    new_population = context.population // len(context.positions)
    for r, c in context.positions:
        context.arr[r][c] = new_population
        new_candidates.add((r, c))


def solution():
    n, l, r = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    cnt = -1
    candidates = deque([(i, j) for i in range(n) for j in range(i % 2, n, 2)])
    while True:
        visit = [[False] * len(arr) for _ in range(len(arr))]
        contexts = []
        for i, j in candidates:
            contexts.append(bfs(arr, visit, i, j, l, r))
        if not contexts:
            break
        new_candidates = set([])
        for context in contexts:
            if len(context.positions) > 1:
                move(context, new_candidates)
        candidates = new_candidates
        cnt += 1
    print(cnt)


if __name__ == "__main__":
    solution()


# nxn 크기의 땅 존재. 표현은 r행 c열. 각 칸에는 나라가 하나씩 존재
# r행 c열에는 A[r][c]명 만큼의 인원이 존재
# 인접한 나라끼리는 국격선 존재 -> 정사각형 모양
#
# 인구 이동
# 국경선을 공유하는 두 나라의 인구 차이가 L명 이상, R명 이하라면, 두 나라가 공유하는 국격선을 하루 오픈
# 국경선 모두 열고 -> 이동 시작
# 인접한 칸을 이동해 연합끼리는 이동 가능 (이동하는 나라끼리는 연합이라고 부름)
# 연합의 각 칸의 인구수 -> (연합 인구수)/(연합 칸 개수). 소수점 버림
# 연합 해체 및 국경선 패쇠
#
# 인구 이동 며칠동안 이어졌는지 구하라