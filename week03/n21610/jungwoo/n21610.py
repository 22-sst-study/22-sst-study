from sys import stdin

input1 = stdin.readline
directions = (
    (0, -1),  # 좌
    (-1, -1),  # 좌상
    (-1, 0),  # 상
    (-1, 1),  # 상우
    (0, 1),  # 우
    (1, 1),  # 우하
    (1, 0),  # 하
    (1, -1),  # 하좌
)
diag = (
    (-1, -1),  # 좌상
    (-1, 1),  # 상우
    (1, 1),  # 우하
    (1, -1),  # 하좌
)


def is_in_range(n, a, b):
    return 0 <= a < n and 0 <= b < n


def solution():
    n, _m = map(int, input1().split())
    arr = [list(map(int, input1().split())) for _ in range(n)]
    moves = [list(map(int, input1().split())) for _ in range(_m)]

    clouds = [(n - 1, 0), (n - 1, 1), (n - 2, 0), (n - 2, 1)]
    for md, ms in moves:
        water_copy_positions = {}
        cloud_removed_positions = set()

        for cr, cc in clouds:
            # step 1. 구름 이동
            x, y = (directions[md - 1][0] * ms + cr) % n, (directions[md - 1][1] * ms + cc) % n
            # step 2. 비 내림
            arr[x][y] += 1
            cloud_removed_positions.add((x, y))
            water_copy_positions[(x, y)] = [(x + _x, y + _y) for _x, _y in diag if is_in_range(n, x + _x, y + _y)]

        # step 3. 구름 사라짐
        clouds.clear()

        # step 4. 물 복사
        for (r, c), copy_positions in water_copy_positions.items():
            arr[r][c] += sum(map(lambda _p: 1 if arr[_p[0]][_p[1]] > 0 else 0, copy_positions))

        # step 5. 구름 생성
        for i in range(n):
            for j in range(n):
                if arr[i][j] >= 2 and (i, j) not in cloud_removed_positions:
                    clouds.append((i, j))
                    arr[i][j] -= 2

    print(sum([sum(a) for a in arr]))


if __name__ == "__main__":
    solution()
