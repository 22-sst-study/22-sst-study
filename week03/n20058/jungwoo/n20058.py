from collections import deque
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


class Counter:
    def __init__(self):
        self.ice = 0
        self.block = 0


def spin(arr, r, c, b):
    for i in range(b // 2):
        for j in range(b // 2):
            arr[i + r][j + c], arr[j + r][b - i - 1 + c], arr[b - i - 1 + r][b - j - 1 + c], arr[b - j - 1 + r][i + c] = \
                arr[b - j - 1 + r][i + c], arr[i + r][j + c], arr[j + r][b - i - 1 + c], arr[b - i - 1 + r][b - j - 1 + c]


def start_magic(arr, block_size):
    for i in range(0, len(arr), block_size):
        for j in range(0, len(arr), block_size):
            spin(arr, i, j, block_size)


def bfs(arr, visit, sr, sc, end_game, cnt):
    q = deque([[(sr, sc)]])
    visit[sr][sc] = True
    updates = []
    while q:
        popped = q.popleft()
        next_pos = []
        for r, c in popped:
            ice_count = 0
            for a, b in directions:
                x, y = r + a, c + b
                if not is_in_range(len(arr), x, y):
                    continue
                if arr[x][y] > 0:
                    ice_count += 1
                    if not visit[x][y]:
                        next_pos.append((x, y))
                visit[x][y] = True
            if end_game:
                cnt.ice += arr[r][c]
                cnt.block += 1
            elif ice_count < 3:
                updates.append((r, c))
        if next_pos:
            q.append(next_pos)
    for r, c in updates:
        arr[r][c] -= 1


def bfs_starter(arr, end_game=False):
    total_ice, max_block = 0, 0
    visit = [[False] * len(arr) for _ in range(len(arr))]
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] > 0 and not visit[i][j]:
                cnt = Counter()
                bfs(arr, visit, i, j, end_game, cnt)
                if end_game:
                    total_ice += cnt.ice
                    max_block = max(max_block, cnt.block)
    return f'{total_ice}\n{max_block}'


def solution():
    n, _ = map(int, input1().split())
    arr = [list(map(int, input1().split())) for _ in range(2 ** n)]
    magics = list(map(int, input1().split()))

    for magic in magics:
        start_magic(arr, 2 ** magic)
        bfs_starter(arr)
    print(bfs_starter(arr, end_game=True))


if __name__ == "__main__":
    solution()
