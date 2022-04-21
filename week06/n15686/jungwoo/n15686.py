from itertools import combinations
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


def get_structure(arr, m):
    shops, homes = [], []
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] == 1:
                home_idx = len(homes)
                homes.append((home_idx, i, j))
            elif arr[i][j] == 2:
                shops.append((len(shops), i, j))
    return list(combinations(shops, m)), shops, homes


def get_distance(total_shops, homes):
    dic = {}
    for home in homes:
        dic[home] = [None] * 13
        for i, shop in enumerate(total_shops):
            dic[home][i] = abs(home[2] - shop[2]) + abs(home[1] - shop[1])
    return dic  # {(1, 1): [2, 3]} -> {홈위치: [치킨거리, 인덱스는 치킨집 인덱스]}


def solution():
    n, m = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]

    candidate_shops, total_shops, homes = get_structure(arr, m)
    distances = get_distance(total_shops, homes)

    answer = 10000000
    for shops in candidate_shops:
        tmp_sum = 0
        for _home, dist in distances.items():
            minimum_dist = 100
            for shop_idx, *shop in shops:
                minimum_dist = min(dist[shop_idx], minimum_dist)
            tmp_sum += minimum_dist
        answer = min(answer, tmp_sum)
    print(answer)


if __name__ == "__main__":
    solution()
