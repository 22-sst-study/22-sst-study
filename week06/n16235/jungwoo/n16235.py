import bisect
from collections import defaultdict
from sys import stdin

input1 = stdin.readline
directions = (
    (0, 1),  # 우
    (-1, 1),  # 우상
    (-1, 0),  # 상
    (-1, -1),  # 상좌
    (0, -1),  # 좌
    (1, -1),  # 좌하
    (1, 0),  # 하
    (1, 1),  # 하우
)


def is_in_range(obj, a, b):
    if isinstance(obj, int):
        return 0 <= a < obj and 0 <= b < obj
    else:
        return 0 <= a < len(obj) and 0 <= b < len(obj)


def make_baby(n, r, c):
    baby, cnt = defaultdict(int), 0
    for a, b in directions:
        x, y = r + a, c + b
        if not is_in_range(n, x, y):
            continue
        baby[x * 100 + y] += 1
        cnt += 1
    return baby, cnt


def add_soil(arr, add):
    for i in range(len(arr)):
        for j in range(len(arr)):
            arr[i][j] += add[i][j]


def solution():
    n, m, k = map(int, input().split())
    add = [list(map(int, input().split())) for _ in range(n)]
    tree = defaultdict(list)
    for _ in range(m):
        r, c, age = map(int, input().split())
        bisect.insort(tree[(r - 1) * 100 + (c - 1)], age)
    arr = [[5] * n for _ in range(n)]

    answer = m
    for K in range(k):
        babies_list = []
        for pos, ages in tree.items():
            r, c = pos // 100, pos % 100
            dead_line, dead_sum = -1, 0
            for i, age in enumerate(ages):
                if arr[r][c] >= age:
                    arr[r][c] -= age
                    ages[i] += 1
                    if ages[i] % 5 == 0:
                        new_baby, new_baby_cnt = make_baby(n, r, c)
                        babies_list.append(new_baby)
                        answer += new_baby_cnt
                else:
                    dead_line = i if dead_line == -1 else dead_line
                    dead_sum += age // 2
            if dead_line != -1:
                answer -= len(tree[pos]) - dead_line
                arr[r][c] += dead_sum
                tree[pos] = tree[pos][:dead_line]

        add_soil(arr, add)
        for babies in babies_list:
            for _pos, cnt in babies.items():
                tree[_pos] = [1] * cnt + tree[_pos]
    print(answer)


if __name__ == "__main__":
    solution()

# nxn 배열
# 양분 조사 로봇
# 로봇은 개별 칸에 대해 양분을 조사해서 전송, 모든 칸에 대해 조사
# 처음 양분은 5 만큼 있음
#
# 나무 재테크
# m개 나무 심음
# 하나의 칸에 여러 나무 심기 가능
#
# 봄: 나무 나이만큼 양분 소모, 나이 1 증가. 나이 어린 나무부터 양분 소모. 양분 없으면 즉사
# 여름: 봄에 죽은 나무가 양분으로 변함. 추가되는 양분 = 각 죽은 나무 나이 // 2
# 가을: 나무 번식. 번식 나무 = 나이가 5의 배수. 인접한 8개의 칸에 나이가 1인 나무 생성. 배열 바깥에는 나무 안 생김
# 겨울: 로봇이 돌아다니면서 양분 추가
#
# k년이 지난 후에 나무의 수는?
