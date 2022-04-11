import itertools
from collections import deque
from sys import stdin

input1 = stdin.readline
directions = (
    (-1, 0),  # 상
    (0, -1),  # 좌
    (1, 0),  # 하
    (0, 1),  # 우
)


def is_in_range(obj, a, b):
    if isinstance(obj, int):
        return 0 <= a < obj and 0 <= b < obj
    else:
        return 0 <= a < len(obj) and 0 <= b < len(obj)


def init(arr):
    target, m_candidates = 0, []
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] == 0:
                target += 1
            elif arr[i][j] == 2:
                m_candidates.append([i, j])
    return target, m_candidates


class Bfs:
    total_cnt = 0

    def __repr__(self):
        return f'({self.r}, {self.c})'

    def __init__(self, arr, visit, r, c, target):
        self.arr, self.visit, self.r, self.c, self.target = arr, visit, r, c, target
        self.q = deque([[(r, c)]])
        self.visit[r][c] = True
        self.time = 0

    def move(self):
        q = self.q
        self.time += 1
        next_positions = []
        for r, c in q.popleft():
            for i in range(4):
                x, y = directions[i][0] + r, directions[i][1] + c
                if not is_in_range(self.arr, x, y) or self.visit[x][y] or self.arr[x][y] not in (0, 2):
                    continue
                self.visit[x][y] = True
                if self.arr[x][y] == 0:
                    Bfs.total_cnt += 1
                next_positions.append((x, y))
        if next_positions:
            q.append(next_positions)


def parallel_bfs(arr, n, m_position, target):  # 동시 bfs
    visit = [[False] * n for _ in range(n)]
    bfs_list = [Bfs(arr, visit, _r, _c, target) for _r, _c in m_position]
    time = 0
    out = set()
    while Bfs.total_cnt < target and len(out) < len(bfs_list):
        time += 1
        for i in range(len(bfs_list)):
            if i not in out:
                bfs_list[i].move()
                if not bfs_list[i].q:
                    out.add(i)
    return Bfs.total_cnt, time


def solution():
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    answer = []

    # 벽을 제외한 나머지 공간의 수 (target)와 바이러스 놓을 수 있는 위치 저장(m_candidates)
    target, m_candidates = init(arr)
    if target == 0:
        print(0)
        return

    # 바이러스 놓을 수 있는 위치 저장
    m_positions = list(itertools.combinations(m_candidates, m))

    # 저장된 위치 중에서 m개를 뽑음
    for m_position in m_positions:
        # 동시 bfs
        result, time = parallel_bfs(arr, n, m_position, target)
        Bfs.total_cnt = 0

        # cnt 수가 target만큼 되면 정답 후보군에 저장
        if result == target:
            answer.append(time)

    # 출력
    print(min(answer) if answer else -1)


if __name__ == "__main__":
    solution()
